# Codex Workflow Prompt — Real-Time Virtual Formal Suit Filter

You are my coding worker. Help me build a beginner-friendly Python computer vision project.

## Project Goal

Build a **real-time virtual formal clothing filter** using my webcam.

I may be wearing casual clothes or a sando, but the webcam output should overlay a **formal suit/tuxedo PNG** on my upper body.

The suit must follow my body while I move.

It should:

* Follow me when I move left or right
* Move when I move up or down
* Resize when I move closer/farther from the camera
* Rotate slightly when I lean
* Stay positioned around my shoulders and torso
* Have smooth movement with minimal shaking
* Work in real-time video

This is for a school video presentation.

---

# Technology

Use:

* Python
* OpenCV
* MediaPipe
* NumPy

Later we may add:

* pyvirtualcam
* OBS Virtual Camera

Do NOT use generative AI or heavy AI models.

Keep the first version lightweight and suitable for a normal laptop.

---

# Project Structure

Create:

```text
virtual-formal-filter/
│
├── main.py
├── requirements.txt
├── README.md
│
├── assets/
│   └── suit.png
│
└── src/
    ├── pose_tracker.py
    ├── clothing_overlay.py
    └── smoothing.py
```

Keep the architecture simple.

Do not overengineer.

---

# Development Workflow

Build this project STEP BY STEP.

Do not implement everything at once.

After every major step:

1. Check the existing code
2. Implement only the current step
3. Explain briefly what changed
4. Tell me how to run/test it
5. Fix errors before continuing

---

# STEP 1 — Webcam

Create a basic OpenCV webcam application.

Requirements:

* Open default webcam
* Display live video
* Press `q` to quit
* Handle camera errors safely

Do not add pose detection yet.

---

# STEP 2 — MediaPipe Pose Detection

Add MediaPipe pose tracking.

Detect:

* Left shoulder
* Right shoulder
* Left hip
* Right hip

Display small debug circles on these landmarks.

Keep webcam FPS reasonably smooth.

---

# STEP 3 — Load Formal Suit PNG

Use:

```text
assets/suit.png
```

The image will have a transparent background.

Load it while preserving the alpha channel.

If the file does not exist, show a clear error message instead of crashing mysteriously.

---

# STEP 4 — Attach Suit to Body

Use the detected landmarks to calculate:

* Shoulder width
* Torso width
* Torso height
* Torso center
* Suit position

Resize the suit automatically according to the user's body size.

The suit should roughly cover:

```text
left shoulder → right shoulder
shoulders → hips
```

Use alpha blending so the transparent PNG overlays correctly on the webcam.

---

# STEP 5 — Body Movement Tracking

Make the suit update every video frame.

The suit must follow:

```text
movement left/right
movement up/down
movement closer/farther
```

Do not use fixed pixel coordinates.

Calculate everything from MediaPipe landmarks.

---

# STEP 6 — Rotation

Calculate the angle between:

```text
left shoulder
right shoulder
```

Rotate the suit slightly when the user leans.

Keep rotation natural and avoid extreme rotation.

---

# STEP 7 — Movement Smoothing

MediaPipe coordinates may jitter.

Create smoothing logic.

Example concept:

```python
smoothed = previous * 0.8 + current * 0.2
```

Smooth:

* x position
* y position
* width
* height
* rotation angle

Make the filter responsive but not shaky.

Put smoothing logic in:

```text
src/smoothing.py
```

---

# STEP 8 — Improve Clothing Alignment

Fine-tune:

* Shoulder offset
* Neck position
* Width multiplier
* Height multiplier
* Hip alignment

Create easy configuration constants near the top of the program, for example:

```python
SUIT_WIDTH_SCALE = 1.4
SUIT_HEIGHT_SCALE = 1.2
SUIT_Y_OFFSET = -20
```

This lets me manually adjust the suit without rewriting the algorithm.

---

# STEP 9 — Performance

Optimize the program so it can run comfortably in real time.

Possible improvements:

* Flip webcam horizontally
* Process a smaller frame if needed
* Avoid loading images every frame
* Avoid unnecessary calculations
* Maintain acceptable FPS

Show FPS on screen for debugging.

---

# STEP 10 — Clean Display Mode

Add keyboard controls.

Example:

```text
Q = quit
D = toggle landmark/debug display
F = toggle FPS display
```

Normal presentation mode should only show:

```text
webcam
+
formal clothing
```

No debugging landmarks.

---

# FUTURE STEP — Virtual Webcam

Do NOT implement this until the main filter works.

Later add:

```text
pyvirtualcam
```

Flow:

```text
Real Webcam
    ↓
Python OpenCV Filter
    ↓
Virtual Camera
    ↓
OBS / Google Meet / Zoom
```

Keep this feature separate from the main pose/filter logic.

---

# Coding Rules

Use clear beginner-friendly Python.

Prefer:

```text
small functions
clear variable names
comments only when useful
simple architecture
```

Avoid:

```text
huge classes
unnecessary abstractions
complex design patterns
large dependencies
```

Before creating new code, inspect existing files first.

Never delete working functionality unless necessary.

When fixing something, make the smallest safe change.

---

# Error Handling

Handle common problems clearly:

* Webcam unavailable
* MediaPipe cannot detect body
* suit.png missing
* PNG has no alpha channel
* Overlay goes outside webcam frame
* Invalid image dimensions

The application should not crash simply because the body temporarily disappears from view.

If no pose is detected, show the original webcam frame.

---

# Target Result

The final result should behave approximately like:

```text
        HEAD
          O
          
    ●-----------●
      \       /
       \ SUIT/
        \   /
         \ /
    ●-----------●
```

The virtual formal clothes should stay attached to the torso while the user naturally moves during a presentation.

Start with **STEP 1 only**.

Inspect the current project directory first, then create the minimum files required for Step 1.

Do not proceed to Step 2 until Step 1 is working.
