"""Run the Meet Capture monitoring loop."""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from capture import capture_monitor
from config import (
    CAPTURE_INTERVAL_SECONDS,
    CHANGE_THRESHOLD,
    SCREENSHOT_DIRECTORY,
    STABILIZATION_DELAY_SECONDS,
)
from detector import has_meaningful_change
from monitor_selector import select_monitor
from storage import save_screenshot


def main() -> None:
    """Select a physical monitor and monitor it until interrupted by the user."""
    selected_monitor = select_monitor()
    if selected_monitor is None:
        return

    print("Meet Capture started.")
    print(f"Monitoring: {selected_monitor.label}")

    try:
        previous_frame = capture_monitor(selected_monitor)
        while True:
            time.sleep(CAPTURE_INTERVAL_SECONDS)
            current_frame = capture_monitor(selected_monitor)

            if not has_meaningful_change(
                previous_frame, current_frame, CHANGE_THRESHOLD
            ):
                previous_frame = current_frame
                continue

            print("\nSlide change detected.")
            time.sleep(STABILIZATION_DELAY_SECONDS)
            stable_frame = capture_monitor(selected_monitor)
            saved_path = save_screenshot(stable_frame, SCREENSHOT_DIRECTORY)
            print(f"Saved: {saved_path.relative_to(SCREENSHOT_DIRECTORY.parent)}")
            previous_frame = stable_frame
    except KeyboardInterrupt:
        print("\nMeet Capture stopped.")


if __name__ == "__main__":
    main()
