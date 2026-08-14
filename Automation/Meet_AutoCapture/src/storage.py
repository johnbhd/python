"""Screenshot naming and saving."""

from pathlib import Path

import cv2
import numpy as np
from PIL import Image


def next_screenshot_path(directory: Path) -> Path:
    """Return the next unused ``slide_XXX.png`` path in ``directory``."""
    directory.mkdir(parents=True, exist_ok=True)
    number = 1
    while (directory / f"slide_{number:03d}.png").exists():
        number += 1
    return directory / f"slide_{number:03d}.png"


def save_screenshot(frame: np.ndarray, directory: Path) -> Path:
    """Save a BGR frame as a new PNG without overwriting an existing slide."""
    destination = next_screenshot_path(directory)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    Image.fromarray(rgb_frame).save(destination)
    return destination
