# Architecture
## Project Structure

virtual-formal-filter/
│
├── main.py
├── requirements.txt
├── README.md
│
├── assets/
│   └── suit.png
│
├── src/
│   ├── pose_tracker.py
│   ├── clothing_overlay.py
│   └── smoothing.py
│
└── workflows/
    ├── ARCHITECTURE.md
    ├── CONTROLS.md
    ├── SETUP.md
    ├── TROUBLESHOOTING.md
    └── WORKFLOW.md
## Main Flow

Webcam
↓
OpenCV captures video
↓
MediaPipe detects body
↓
Get shoulders and hips
↓
Calculate body position
↓
Resize and rotate suit
↓
Smooth movement
↓
Overlay suit on video
↓
Display final video

## Main Files

### main.py
Main application.

Responsible for:
- Opening the webcam
- Reading video frames
- Running body tracking
- Adding the suit
- Showing the final video

### pose_tracker.py
Handles body detection using MediaPipe.

Tracks:
- Left shoulder
- Right shoulder
- Left hip
- Right hip

### clothing_overlay.py
Handles the virtual clothes.

Responsible for:
- Loading `suit.png`
- Resizing the suit
- Rotating the suit
- Positioning it on the body
- Adding it to the webcam frame

### smoothing.py
Reduces shaking or jitter from body tracking.

This makes the suit follow the body more smoothly.

## Assets

`assets/suit.png`

The suit image should:
- Have a transparent background
- Face forward
- Show the upper formal clothing clearly