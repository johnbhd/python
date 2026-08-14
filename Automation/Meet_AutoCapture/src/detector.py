"""Frame comparison for presentation slide changes."""

import cv2
import numpy as np


def change_score(previous_frame: np.ndarray, current_frame: np.ndarray) -> float:
    """Return the mean grayscale pixel difference between two frames."""
    previous_small = cv2.resize(previous_frame, (320, 180))
    current_small = cv2.resize(current_frame, (320, 180))

    previous_gray = cv2.cvtColor(previous_small, cv2.COLOR_BGR2GRAY)
    current_gray = cv2.cvtColor(current_small, cv2.COLOR_BGR2GRAY)
    difference = cv2.absdiff(previous_gray, current_gray)
    return float(np.mean(difference))


def has_meaningful_change(
    previous_frame: np.ndarray, current_frame: np.ndarray, threshold: float
) -> bool:
    """Return True when the frame difference meets the configured threshold."""
    return change_score(previous_frame, current_frame) >= threshold
