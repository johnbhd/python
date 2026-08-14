"""Physical-monitor capture using MSS."""

import mss
import numpy as np

from monitor_selector import Monitor


def capture_monitor(monitor: Monitor) -> np.ndarray:
    """Capture the entire selected physical monitor as a BGR frame."""
    with mss.mss() as screen_capture:
        raw_frame = np.asarray(screen_capture.grab(monitor.bounds))

    # MSS supplies BGRA pixels; OpenCV comparisons and image saving use BGR.
    return raw_frame[:, :, :3]
