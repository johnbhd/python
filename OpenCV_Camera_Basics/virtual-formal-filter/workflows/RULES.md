# Coding Rules

## General

- Keep the project simple.
- Do not overengineer.
- Prefer readable code over clever code.
- Use clear and descriptive variable names.
- Keep functions small and focused on one task.
- Avoid duplicate code.
- Remove unused imports, variables, and functions.
- Do not create unnecessary files or folders.

## File Responsibilities

### main.py
Only handle:
- Application startup
- Webcam loop
- Connecting project components
- Keyboard controls

Do not put large image-processing logic directly in main.py.

### src/pose_tracker.py
Only handle:
- MediaPipe setup
- Pose detection
- Shoulder and hip landmarks
- Pose coordinates

### src/clothing_overlay.py
Only handle:
- Loading clothing images
- Resizing
- Rotation
- Positioning
- Alpha blending

### src/smoothing.py
Only handle:
- Coordinate smoothing
- Reducing tracking jitter

## Functions

Prefer small functions.

Good:

```python
detect_pose()
get_torso_points()
resize_suit()
rotate_suit()
overlay_suit()

Avoid one huge function that performs the entire application.

Naming

Use Python snake_case.

Good:

left_shoulder
torso_width
suit_image
calculate_rotation()

Avoid:

ls
tw
img2
doStuff()
Constants

Configuration values should be easy to find.

Example:

CAMERA_INDEX = 0
SUIT_WIDTH_SCALE = 1.4
SUIT_HEIGHT_SCALE = 1.2
SUIT_Y_OFFSET = -20
SMOOTHING_FACTOR = 0.8

Do not scatter magic numbers throughout the code.

Error Handling

Handle expected errors clearly.

Examples:

Webcam unavailable
Missing suit image
Invalid PNG
Pose temporarily not detected
Overlay outside frame

Do not silently ignore errors.

Computer Vision Rules
Do not reload the suit PNG every frame.
Load assets once during startup.
Do not initialize MediaPipe every frame.
Reuse the pose tracker.
Check coordinates before accessing image regions.
Safely crop overlays near frame edges.
Preserve the PNG alpha channel.
Keep real-time performance in mind.
Performance
Avoid unnecessary work inside the webcam loop.
Avoid repeatedly creating heavy objects.
Keep webcam processing lightweight.
Optimize only when needed.
Prefer understandable code before premature optimization.
Changes

Before modifying code:

Inspect the existing implementation.
Understand which file owns the functionality.
Make the smallest reasonable change.
Do not rewrite working code unnecessarily.
Preserve existing working features.
Test after meaningful changes.
Dependencies

Do not install a new library unless it provides a clear benefit.

Current main dependencies:

opencv-python
mediapipe
numpy

Future:

pyvirtualcam

Avoid adding large AI frameworks unless the project actually requires them.

Comments

Use comments to explain WHY something is done.

Avoid comments that simply repeat the code.

Good:

# Smooth landmark movement to prevent the suit from visibly jittering.

Avoid:

# Set width
width = 500
Development Rule

Build one working stage at a time.

Do not implement future features before the current stage works.

Follow:

workflows/WORKFLOW.md

Final Rule

Keep this project:

Beginner-friendly
Modular
Easy to debug
Easy to modify
Lightweight
Clean

If a solution makes the project significantly more complicated without a clear benefit, choose the simpler solution.


So the separation is:

```text
AGENTS.md
→ HOW Codex should write and modify code

WORKFLOW.md
→ WHAT Codex should build next

ARCHITECTURE.md
→ WHERE code belongs

SETUP.md
→ HOW to install/run

TROUBLESHOOTING.md
→ HOW to fix common problems