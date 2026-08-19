"""Record filtered video and microphone audio using a shared real-time clock."""

import math
import shutil
import subprocess
import time
from datetime import datetime
from pathlib import Path

import cv2
import numpy as np

try:
    import sounddevice as sd
    import soundfile as sf
except ImportError:
    sd = None
    sf = None


RECORDING_FPS = 30
AUDIO_SAMPLE_RATE = 44100
AUDIO_CHANNELS = 1
AUDIO_DEVICE = None
VIDEO_CODEC = "mp4v"


class Recorder:
    """Create a real-time recording without tying output duration to processing FPS."""

    def __init__(self, recordings_directory: Path) -> None:
        self._recordings_directory = recordings_directory
        self._video_writer = None
        self._audio_stream = None
        self._audio_chunks = []
        self._record_start_time = None
        self._frames_written = 0
        self._last_frame = None
        self._temporary_video_path = None
        self._temporary_audio_path = None
        self._final_path = None

    @property
    def is_recording(self) -> bool:
        """Return whether recording resources are currently active."""
        return self._video_writer is not None

    def start(self, frame) -> Path:
        """Start synchronized video and microphone capture for a clean frame."""
        if sd is None or sf is None:
            raise RuntimeError(
                "Microphone recording requires sounddevice and soundfile. "
                "Run: pip install -r requirements.txt"
            )

        self._recordings_directory.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")
        self._temporary_video_path = (
            self._recordings_directory / f"temp_video_{timestamp}.mp4"
        )
        self._temporary_audio_path = (
            self._recordings_directory / f"temp_audio_{timestamp}.wav"
        )
        self._final_path = self._recordings_directory / f"recording_{timestamp}.mp4"
        self._video_writer = self._create_video_writer(frame)
        self._audio_chunks = []
        self._frames_written = 0
        self._last_frame = frame.copy()

        try:
            self._record_start_time = time.perf_counter()
            self._audio_stream = sd.InputStream(
                samplerate=AUDIO_SAMPLE_RATE,
                channels=AUDIO_CHANNELS,
                device=AUDIO_DEVICE,
                dtype="float32",
                callback=self._capture_audio,
            )
            self._audio_stream.start()
        except Exception:
            self._release_recording_resources()
            raise

        self.write_frame(frame)
        return self._final_path

    def write_frame(self, frame) -> None:
        """Write enough copies of the newest frame to match elapsed real time."""
        if not self.is_recording:
            return

        self._last_frame = frame.copy()
        elapsed_time = time.perf_counter() - self._record_start_time
        expected_frame_count = max(1, math.ceil(elapsed_time * RECORDING_FPS))
        frames_to_write = expected_frame_count - self._frames_written
        for _ in range(max(0, frames_to_write)):
            self._video_writer.write(self._last_frame)
            self._frames_written += 1

    def stop(self, frame) -> Path | None:
        """Finish recording, then mux the temporary video and audio into an MP4."""
        if not self.is_recording:
            return None

        self.write_frame(frame)
        self._video_writer.release()
        self._video_writer = None
        self._stop_audio_stream()

        try:
            self._save_audio()
            self._mux_recording()
        except RuntimeError as error:
            print(f"Recording not finalized: {error}")
            return None

        self._temporary_video_path.unlink()
        self._temporary_audio_path.unlink()
        return self._final_path

    def _create_video_writer(self, frame) -> cv2.VideoWriter:
        """Create a fixed-FPS writer for the filtered frame dimensions."""
        frame_height, frame_width = frame.shape[:2]
        codec = cv2.VideoWriter_fourcc(*VIDEO_CODEC)
        video_writer = cv2.VideoWriter(
            str(self._temporary_video_path),
            codec,
            RECORDING_FPS,
            (frame_width, frame_height),
        )
        if not video_writer.isOpened():
            video_writer.release()
            raise RuntimeError("Could not create the temporary MP4 video file.")
        return video_writer

    def _capture_audio(self, indata, frames, time_info, status) -> None:
        """Copy microphone samples quickly so the callback never blocks the preview."""
        if status:
            print(f"Audio input warning: {status}")
        self._audio_chunks.append(indata.copy())

    def _stop_audio_stream(self) -> None:
        """Stop the microphone callback before saving its captured samples."""
        if self._audio_stream is not None:
            self._audio_stream.stop()
            self._audio_stream.close()
            self._audio_stream = None

    def _save_audio(self) -> None:
        """Save callback samples as a WAV file for FFmpeg to mux."""
        if not self._audio_chunks:
            raise RuntimeError("No microphone audio was captured.")

        audio_samples = np.concatenate(self._audio_chunks, axis=0)
        sf.write(self._temporary_audio_path, audio_samples, AUDIO_SAMPLE_RATE)

    def _mux_recording(self) -> None:
        """Combine temporary video and WAV audio without changing their time base."""
        ffmpeg_path = shutil.which("ffmpeg")
        print(f"FFmpeg detected: {ffmpeg_path}")
        if ffmpeg_path is None:
            self._raise_merge_error(
                "FFmpeg is required to merge video and audio. Install FFmpeg and "
                "add it to PATH."
            )

        print("Merging audio and video...")
        mux_result = self._run_ffmpeg(self._build_ffmpeg_command(ffmpeg_path, "copy"))
        if mux_result.returncode != 0:
            print("Video stream copy failed. Retrying with H.264 encoding...")
            mux_result = self._run_ffmpeg(
                self._build_ffmpeg_command(ffmpeg_path, "libx264")
            )

        if mux_result.returncode != 0:
            self._final_path.unlink(missing_ok=True)
            self._raise_merge_error(mux_result.stderr)

        if not self._final_path.is_file() or self._final_path.stat().st_size == 0:
            self._final_path.unlink(missing_ok=True)
            self._raise_merge_error(
                "FFmpeg returned success but did not create a valid MP4."
            )

        print(f"Merge successful: {self._final_path}")

    def _build_ffmpeg_command(
        self,
        ffmpeg_path: str,
        video_codec: str,
    ) -> list[str]:
        """Build the compatible MP4 mux command for the selected video codec."""
        command = [
            ffmpeg_path,
            "-y",
            "-i",
            str(self._temporary_video_path),
            "-i",
            str(self._temporary_audio_path),
            "-c:v",
            video_codec,
        ]
        if video_codec == "libx264":
            command.extend(["-preset", "fast"])
        command.extend([
            "-c:a",
            "aac",
            "-shortest",
            "-movflags",
            "+faststart",
            str(self._final_path),
        ])
        return command

    def _run_ffmpeg(self, command: list[str]) -> subprocess.CompletedProcess:
        """Run FFmpeg and retain its complete diagnostics for failure reporting."""
        try:
            mux_result = subprocess.run(command, capture_output=True, text=True)
        except OSError as error:
            self._raise_merge_error(str(error))

        print(f"FFmpeg return code: {mux_result.returncode}")
        if mux_result.stdout:
            print(f"FFmpeg output:\n{mux_result.stdout}")
        if mux_result.stderr:
            print(f"FFmpeg error:\n{mux_result.stderr}")
        return mux_result

    def _raise_merge_error(self, error_message: str) -> None:
        """Report a failed mux while preserving its temporary input files."""
        print("FFmpeg merge failed.")
        print(f"Temporary video: {self._temporary_video_path}")
        print(f"Temporary audio: {self._temporary_audio_path}")
        print(f"FFmpeg error: {error_message}")
        raise RuntimeError("FFmpeg could not merge the recording.")

    def _release_recording_resources(self) -> None:
        """Clean up partially started resources after a start failure."""
        if self._video_writer is not None:
            self._video_writer.release()
            self._video_writer = None
        self._stop_audio_stream()
