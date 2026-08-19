"""Load formal clothing images while preserving transparency."""

from math import dist
from pathlib import Path
from typing import Optional

import cv2
import numpy as np


ALPHA_CHANNEL_COUNT = 4
REQUIRED_SHOULDER_POINTS = ("left_shoulder", "right_shoulder")


def load_suit_image(image_path: Path):
    """Load a transparent suit PNG and validate its image channels."""
    if not image_path.is_file():
        raise FileNotFoundError(
            f"Suit image not found: {image_path}. "
            "Add a transparent PNG at assets/suit.png."
        )

    suit_image = cv2.imread(str(image_path), cv2.IMREAD_UNCHANGED)
    if suit_image is None:
        raise ValueError(f"Could not read the suit image: {image_path}")

    if suit_image.ndim != 3 or suit_image.shape[2] != ALPHA_CHANNEL_COUNT:
        raise ValueError(
            f"Suit image must be a PNG with an alpha channel: {image_path}"
        )

    height, width = suit_image.shape[:2]
    if height == 0 or width == 0:
        raise ValueError(f"Suit image has invalid dimensions: {image_path}")

    return suit_image


def get_shoulder_measurements(
    torso_points: dict[str, tuple[int, int]],
) -> Optional[tuple[float, float, float]]:
    """Return the shoulder midpoint and distance used to place the suit."""
    if not all(point_name in torso_points for point_name in REQUIRED_SHOULDER_POINTS):
        return None

    left_shoulder = torso_points["left_shoulder"]
    right_shoulder = torso_points["right_shoulder"]
    center_x = (left_shoulder[0] + right_shoulder[0]) / 2
    center_y = (left_shoulder[1] + right_shoulder[1]) / 2
    shoulder_width = dist(left_shoulder, right_shoulder)
    return center_x, center_y, shoulder_width


def calculate_suit_position(
    shoulder_center_x: float,
    shoulder_center_y: float,
    shoulder_width: float,
    suit_image,
    left_shoulder_x: float,
    right_shoulder_x: float,
    shoulder_y: float,
    width_scale: float,
    height_scale: float,
    x_offset: int,
    y_offset: int,
) -> Optional[tuple[int, int, int, int]]:
    """Map the suit's internal shoulder anchors to smoothed measurements."""
    if not 0 <= left_shoulder_x < right_shoulder_x <= 1:
        raise ValueError("Suit shoulder X anchors must be between 0 and 1.")
    if not 0 <= shoulder_y <= 1:
        raise ValueError("Suit shoulder Y anchor must be between 0 and 1.")
    if width_scale <= 0 or height_scale <= 0:
        raise ValueError("Suit width and height scales must be greater than 0.")

    image_height, image_width = suit_image.shape[:2]
    anchor_width = image_width * (right_shoulder_x - left_shoulder_x)

    # Apply the two fit controls as one scale so resizing never stretches the
    # transparent PNG. The height is always derived from the source aspect ratio.
    fit_scale = width_scale * height_scale
    suit_scale = shoulder_width / anchor_width * fit_scale
    suit_width = max(1, int(image_width * suit_scale))
    suit_height = max(1, int(image_height * suit_scale))

    anchor_center_x = image_width * (left_shoulder_x + right_shoulder_x) / 2
    suit_x = int(shoulder_center_x - anchor_center_x * suit_scale + x_offset)
    suit_y = int(shoulder_center_y - image_height * shoulder_y * suit_scale + y_offset)
    return suit_x, suit_y, suit_width, suit_height


def resize_suit(suit_image, width: int, height: int):
    """Resize the suit image to fit the detected torso."""
    return cv2.resize(suit_image, (width, height), interpolation=cv2.INTER_AREA)


def overlay_suit(frame, suit_image, suit_x: int, suit_y: int) -> None:
    """Alpha-blend a suit image onto a frame, safely clipping at its edges."""
    suit_height, suit_width = suit_image.shape[:2]
    frame_height, frame_width = frame.shape[:2]

    frame_x_start = max(suit_x, 0)
    frame_y_start = max(suit_y, 0)
    frame_x_end = min(suit_x + suit_width, frame_width)
    frame_y_end = min(suit_y + suit_height, frame_height)

    if frame_x_start >= frame_x_end or frame_y_start >= frame_y_end:
        return

    suit_x_start = frame_x_start - suit_x
    suit_y_start = frame_y_start - suit_y
    suit_x_end = suit_x_start + (frame_x_end - frame_x_start)
    suit_y_end = suit_y_start + (frame_y_end - frame_y_start)

    suit_region = suit_image[suit_y_start:suit_y_end, suit_x_start:suit_x_end]
    frame_region = frame[frame_y_start:frame_y_end, frame_x_start:frame_x_end]
    alpha = suit_region[:, :, 3:4].astype(np.float32) / 255.0

    frame_region[:] = (
        suit_region[:, :, :3] * alpha + frame_region * (1 - alpha)
    ).astype(np.uint8)
