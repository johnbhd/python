"""Replace a webcam background while keeping the detected person visible."""

from pathlib import Path

import cv2
import mediapipe as mp
import numpy as np


SEGMENTATION_THRESHOLD = 0.65
TEMPORAL_SMOOTHING = 0.85
FEATHER_RANGE = 0.10
MASK_BLUR_SIZE = 5
MORPH_KERNEL_SIZE = 3


class BackgroundReplacer:
    """Use MediaPipe selfie segmentation to composite a saved background image."""

    def __init__(self, background_path: Path) -> None:
        self._background_image = None
        self.error_message = None
        if not background_path.is_file():
            self.error_message = f"Background image not found: {background_path}"
        else:
            self._background_image = cv2.imread(str(background_path))
            if self._background_image is None:
                self.error_message = f"Could not read background image: {background_path}"

        self._resized_background = None
        self._background_size = None
        self._previous_mask = None
        self._segmenter = mp.solutions.selfie_segmentation.SelfieSegmentation(
            model_selection=1
        )

    @property
    def is_available(self) -> bool:
        """Return whether the background image loaded successfully."""
        return self._background_image is not None

    def replace_background(self, frame):
        """Return a frame with the person composited over the saved background."""
        if not self.is_available:
            return frame

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        segmentation_result = self._segmenter.process(rgb_frame)
        if segmentation_result.segmentation_mask is None:
            return frame

        background = self._get_resized_background(frame.shape)
        alpha = self._refine_mask(segmentation_result.segmentation_mask)
        return (frame * alpha + background * (1.0 - alpha)).astype(np.uint8)

    def _refine_mask(self, segmentation_mask):
        """Stabilize the float mask while keeping only its boundary feathered."""
        current_mask = segmentation_mask.astype(np.float32)
        smoothed_mask = self._smooth_mask(current_mask)
        kernel = np.ones((MORPH_KERNEL_SIZE, MORPH_KERNEL_SIZE), np.uint8)

        # Closing fills small gaps without eroding hair, shoulders, or clothing.
        smoothed_mask = cv2.morphologyEx(
            smoothed_mask,
            cv2.MORPH_CLOSE,
            kernel,
        )
        alpha = np.clip(
            (smoothed_mask - (SEGMENTATION_THRESHOLD - FEATHER_RANGE))
            / (2.0 * FEATHER_RANGE),
            0.0,
            1.0,
        )
        alpha = cv2.GaussianBlur(
            alpha,
            (MASK_BLUR_SIZE, MASK_BLUR_SIZE),
            0,
        )
        return alpha[:, :, np.newaxis]

    def _smooth_mask(self, current_mask):
        """Smooth segmentation changes without retaining a moving foreground trail."""
        if (
            self._previous_mask is None
            or self._previous_mask.shape != current_mask.shape
        ):
            self._previous_mask = current_mask
            return current_mask

        smoothed_mask = (
            self._previous_mask * TEMPORAL_SMOOTHING
            + current_mask * (1.0 - TEMPORAL_SMOOTHING)
        )
        # Do not let an old foreground position remain opaque after the person moves.
        smoothed_mask = np.minimum(smoothed_mask, current_mask + FEATHER_RANGE)
        self._previous_mask = smoothed_mask
        return smoothed_mask

    def _get_resized_background(self, frame_shape):
        """Resize and cache the background for the current webcam dimensions."""
        frame_height, frame_width = frame_shape[:2]
        background_size = (frame_width, frame_height)
        if background_size != self._background_size:
            self._resized_background = cv2.resize(
                self._background_image,
                background_size,
                interpolation=cv2.INTER_AREA,
            )
            self._background_size = background_size

        return self._resized_background

    def close(self) -> None:
        """Release MediaPipe resources when the application exits."""
        self._segmenter.close()
