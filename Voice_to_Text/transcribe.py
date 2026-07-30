from __future__ import annotations

import argparse
from pathlib import Path

from faster_whisper import WhisperModel


def format_srt_timestamp(seconds: float) -> str:
    """Convert seconds into SRT timestamp format."""
    milliseconds = int(seconds * 1000)

    hours = milliseconds // 3_600_000
    milliseconds %= 3_600_000

    minutes = milliseconds // 60_000
    milliseconds %= 60_000

    secs = milliseconds // 1_000
    milliseconds %= 1_000

    return f"{hours:02}:{minutes:02}:{secs:02},{milliseconds:03}"


def transcribe_audio(
    audio_path: Path,
    model_name: str,
    language: str | None,
) -> None:
    if not audio_path.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    print(f"Loading Whisper model: {model_name}")

    # CPU + INT8 is suitable for laptops without a powerful NVIDIA GPU.
    model = WhisperModel(
        model_name,
        device="cpu",
        compute_type="int8",
        download_root="models",
    )

    print(f"Transcribing: {audio_path.name}")

    segments, info = model.transcribe(
        str(audio_path),
        language=language,
        beam_size=5,
        vad_filter=True,
        condition_on_previous_text=True,
    )

    txt_path = audio_path.with_suffix(".txt")
    srt_path = audio_path.with_suffix(".srt")

    print(
        f"Detected language: {info.language} "
        f"({info.language_probability:.2%} confidence)"
    )

    with (
        txt_path.open("w", encoding="utf-8") as txt_file,
        srt_path.open("w", encoding="utf-8") as srt_file,
    ):
        for number, segment in enumerate(segments, start=1):
            text = segment.text.strip()

            if not text:
                continue

            timestamp = (
                f"[{format_srt_timestamp(segment.start)}"
                f" → {format_srt_timestamp(segment.end)}]"
            )

            print(f"{timestamp} {text}")

            # Plain transcript with timestamps
            txt_file.write(f"{timestamp} {text}\n")

            # Subtitle format
            srt_file.write(f"{number}\n")
            srt_file.write(
                f"{format_srt_timestamp(segment.start)} --> "
                f"{format_srt_timestamp(segment.end)}\n"
            )
            srt_file.write(f"{text}\n\n")

    print("\nTranscription completed.")
    print(f"Text transcript: {txt_path}")
    print(f"Subtitle file:   {srt_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Privately transcribe audio using local Whisper."
    )

    parser.add_argument(
        "audio",
        type=Path,
        help="Path to the audio or video recording.",
    )

    parser.add_argument(
        "--model",
        default="small",
        choices=["tiny", "base", "small", "medium", "large-v3", "turbo"],
        help="Whisper model to use. Default: small",
    )

    parser.add_argument(
        "--language",
        default=None,
        help=(
            "Optional language code such as en or tl. "
            "Leave empty for automatic detection."
        ),
    )

    args = parser.parse_args()

    try:
        transcribe_audio(
            audio_path=args.audio,
            model_name=args.model,
            language=args.language,
        )
    except Exception as error:
        print(f"\nError: {error}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()