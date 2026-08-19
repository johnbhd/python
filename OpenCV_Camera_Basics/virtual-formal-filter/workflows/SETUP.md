# Setup

## Requirements

- Python
- Webcam
- VS Code or terminal

## 1. Create Virtual Environment

```bash
py -m venv .venv

Activate it in PowerShell:

.\.venv\Scripts\Activate.ps1
2. Install Dependencies
pip install opencv-python mediapipe numpy

Later, virtual camera support may use:

pip install pyvirtualcam
3. Install From requirements.txt
pip install -r requirements.txt
4. Add Suit Image

Place the formal clothing image here:

assets/suit.png

The image should use a transparent background.

5. Run
python main.py

Press:

Q

to close the application.

Recommended Suit Image

Use a front-facing:

Tuxedo
Blazer
Formal coat
Dress shirt with coat

Transparent PNG works best.