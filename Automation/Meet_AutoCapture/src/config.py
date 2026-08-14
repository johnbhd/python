"""Settings for the Meet Capture monitor."""

from pathlib import Path

CAPTURE_INTERVAL_SECONDS = 0.5
CHANGE_THRESHOLD = 12.0
STABILIZATION_DELAY_SECONDS = 1.0
SCREENSHOT_DIRECTORY = Path(__file__).resolve().parent.parent / "screenshots"
