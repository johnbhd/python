# Meet AutoCapture

Meet AutoCapture is a local Python tool that watches one physical monitor and automatically saves a screenshot when the display changes significantly. It is useful for capturing presentation slides during online classes, meetings, or demonstrations.

The program captures only the monitor you select. It does not capture a combined multi-monitor desktop.

## Features

- Detects physical monitors with MSS.
- Lets you select a monitor with the Up/Down arrow keys and Enter when multiple displays are available.
- Automatically uses the only monitor when one display is connected.
- Detects meaningful visual changes with OpenCV.
- Waits for the display to stabilize before saving a screenshot.
- Stores screenshots as `slide_001.png`, `slide_002.png`, and so on.
- Stops safely with `Ctrl+C`.

## Requirements

- Windows
- Python 3.12 or later

## Installation

Open PowerShell in the project folder (the folder containing `main.py` and `requirements.txt`). For example:

```powershell
cd path\to\Meet_AutoCapture
```

Create and activate a virtual environment:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run this once for the current terminal, then activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Install the required packages:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run

With the virtual environment activated, run:

```powershell
python main.py
```

If more than one monitor is connected, select one with the arrow keys and press Enter. Press `Ctrl+C` at any time to stop monitoring.

## Configuration

Edit `src/config.py` to adjust:

- `CAPTURE_INTERVAL_SECONDS` — time between screen checks.
- `CHANGE_THRESHOLD` — higher values make detection less sensitive.
- `STABILIZATION_DELAY_SECONDS` — wait time before saving a changed display.
- `SCREENSHOT_DIRECTORY` — destination folder for captures.

## Screenshots

Captured images are stored in the `screenshots/` folder. Existing images are not overwritten; the next available slide number is used automatically.

## Project Structure

```text
Meet_AutoCapture/
├── main.py
├── requirements.txt
├── screenshots/
└── src/
    ├── capture.py
    ├── config.py
    ├── detector.py
    ├── monitor_selector.py
    └── storage.py
```
