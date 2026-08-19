### `TROUBLESHOOTING.md`

```md
# Troubleshooting

## Webcam Does Not Open

Check if another application is using the camera.

Close programs such as:

- Zoom
- Google Meet
- OBS
- Camera app

Then run the program again.

## Wrong Camera

Try another camera index.

Example:

```python
cv2.VideoCapture(0)

Change 0 to:

cv2.VideoCapture(1)
Body Is Not Detected

Make sure:

Your shoulders are visible
Your upper body is visible
Lighting is good
You are facing the camera
You are not too close to the camera
Suit Does Not Appear

Check that this file exists:

assets/suit.png

The PNG should also have transparency.

Suit Is Too Large

Reduce:

SUIT_WIDTH_SCALE
SUIT_HEIGHT_SCALE
Suit Is Too Small

Increase:

SUIT_WIDTH_SCALE
SUIT_HEIGHT_SCALE
Suit Is Too High or Too Low

Adjust:

SUIT_Y_OFFSET
Suit Is Shaking

Body landmarks can slightly change every frame.

Use smoothing to reduce this movement.

Video Is Lagging

Try:

Lower webcam resolution
Close other heavy applications
Reduce image processing
Avoid running unnecessary programs
Suit Disappears Near Screen Edge

The overlay must safely crop the suit when part of it goes outside the webcam frame.