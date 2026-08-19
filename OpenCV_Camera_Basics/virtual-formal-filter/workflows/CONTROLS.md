# Controls

| Key | Action |
|---|---|
| Q | Quit application and save an active recording |
| R | Start recording; press again to stop and save |
| B | Enable or disable background replacement |

## Performance Display

Set `SHOW_FPS = True` in `main.py` to display the current FPS while testing.

## Presentation Mode

Presentation mode should only show:

- Webcam
- Virtual formal suit

No body landmarks or debugging information should appear.

## Recording

Recordings are saved as MP4 files in the `recordings/` folder. A red `REC`
indicator appears in the preview while recording, but is not written to the
saved video.

## Background Replacement

Background replacement is enabled by default. Add the desired image at
`assets/background.jpg`; the application resizes it to match the webcam frame.
Press B to return to the normal webcam background or enable replacement again.
