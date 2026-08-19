The recorder still leaves separate video and audio files after recording.

I want ONE final MP4 containing both video and microphone audio.

Inspect src/recorder.py and diagnose why the FFmpeg merge is not completing.

Do not change the suit filter, background replacement, tracking, or recording timing.

Requirements:

1. When recording stops, always attempt:

temporary video MP4
+
temporary audio WAV
↓
FFmpeg
↓
final recording MP4

2. Detect FFmpeg using:

shutil.which("ffmpeg")

Print the detected FFmpeg path before muxing.

If None, print a clear error.

3. Run FFmpeg with subprocess.run and capture:

- return code
- stdout
- stderr

If FFmpeg fails, print the full stderr so I can see the actual reason.

4. Use a command equivalent to:

ffmpeg -y
-i temp_video.mp4
-i temp_audio.wav
-c:v copy
-c:a aac
-shortest
final_recording.mp4

5. If `-c:v copy` fails because of codec/container compatibility, automatically retry with:

-c:v libx264
-preset fast
-c:a aac

6. After FFmpeg returns success, verify:

final_recording.mp4 exists
AND
final_recording.mp4 file size > 0

Only then consider the merge successful.

7. On successful merge:

delete temporary video
delete temporary WAV

The recordings folder should contain only:

recording_YYYY-MM-DD_HH-MM-SS.mp4

8. On merge failure:

DO NOT delete the temporary files.

Print:

FFmpeg merge failed.
Temporary video: ...
Temporary audio: ...
FFmpeg error: ...

9. Pressing Q while recording must use exactly the same finalize-and-merge process.

10. Do not silently catch FFmpeg errors.

I need the terminal to clearly show:

FFmpeg detected: ...
Merging audio and video...
Merge successful: recordings/recording_xxx.mp4

or the exact FFmpeg error if it fails.

Follow AGENTS.md and make the smallest clean fix.