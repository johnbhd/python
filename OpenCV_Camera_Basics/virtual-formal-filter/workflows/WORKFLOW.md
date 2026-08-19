# Development Workflow

## Step 1 - Webcam

Open and display the default webcam with OpenCV. Press `Q` to quit.

## Step 2 - Body Detection

Use MediaPipe Pose to detect the shoulders and hips. Show landmark debug circles.

## Step 3 - Load Suit

Load `assets/suit.png` once, preserving its alpha channel. Show clear errors when the file is missing or invalid.

## Step 4 - Attach Suit

Attach the suit using the two shoulder landmarks and the PNG's internal shoulder anchors. Keep alignment constants easy to adjust.

## Step 5 - Movement Tracking

Recalculate the suit from the two shoulders on every frame so it follows left/right and up/down movement and resizes as the user moves closer or farther from the camera.

## Step 6 - Smoothing and Jitter Reduction

Reduce visible jitter while keeping the suit responsive. Smooth its X position, Y position, width, and height. Put the smoothing logic in `src/smoothing.py`.

## Step 7 - Improve Alignment

Fine-tune the shoulder anchors, width scale, height scale, and X/Y offsets using the configuration constants in `main.py`.

## Step 8 - Performance

Keep the application comfortable to run in real time. Avoid loading assets or creating heavy objects inside the frame loop. Add FPS display only when this step begins.

## Step 9 - Presentation Mode

Normal presentation mode should show only the webcam and formal suit. Keep FPS
disabled unless it is needed for performance testing.

## Step 10 - Video Recording

Record the final filtered webcam frame with OpenCV VideoWriter. Save each MP4
recording in `recordings/` with a date-and-time filename. Use R to start and
stop recording, and safely release an active recording when Q closes the app.

## Step 11 - Background Replacement

Use MediaPipe selfie segmentation to replace the original webcam background
with `assets/background.jpg`. Keep the person and formal suit visible, default
replacement to on, and use B to toggle it without affecting recording.

## Future - Virtual Camera

After the main filter works reliably, optionally add `pyvirtualcam` for OBS, Google Meet, or Zoom.
