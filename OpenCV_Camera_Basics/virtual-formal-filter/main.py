"""Application entry point for the virtual formal suit filter."""

import sys
import time
from pathlib import Path

import cv2

from src.background_replacer import BackgroundReplacer
from src.clothing_overlay import (
    calculate_suit_position,
    get_shoulder_measurements,
    load_suit_image,
    overlay_suit,
    resize_suit,
)
from src.pose_tracker import PoseTracker
from src.recorder import Recorder
from src.smoothing import SuitSmoother


CAMERA_INDEX = 0
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
WINDOW_TITLE = "Virtual Formal Suit Filter - Step 11"
SUIT_IMAGE_PATH = Path(__file__).parent / "assets" / "suit.png"
BACKGROUND_IMAGE_PATH = Path(__file__).parent / "assets" / "background.jpg"
BACKGROUND_REPLACEMENT_ENABLED = True

# Suit fit and alignment configuration. Adjust these values together while the
# webcam is running to match the transparent PNG to your shoulders and collar.
# Both size scales contribute to one uniform scale so the PNG keeps its aspect
# ratio: use width scale for shoulder coverage and height scale for overall
# vertical coverage tuning.
SUIT_LEFT_SHOULDER_X = 0.20
SUIT_RIGHT_SHOULDER_X = 0.80
SUIT_SHOULDER_Y = 0.20
SUIT_WIDTH_SCALE = 1.0
SUIT_HEIGHT_SCALE = 1.0
SUIT_X_OFFSET = -15
SUIT_Y_OFFSET = -120

SMOOTHING_FACTOR = 0.35
SHOW_FPS = False
FPS_UPDATE_INTERVAL = 0.5
FPS_TEXT_POSITION = (10, 30)
FPS_TEXT_COLOR = (0, 255, 0)
FPS_TEXT_SCALE = 0.7
FPS_TEXT_THICKNESS = 2
RECORDINGS_DIRECTORY = Path(__file__).parent / "recordings"
REC_TEXT = "REC"
REC_TEXT_POSITION = (10, 60)
REC_TEXT_COLOR = (0, 0, 255)
REC_TEXT_SCALE = 0.7
REC_TEXT_THICKNESS = 2


def draw_fps(frame, fps: float) -> None:
    """Draw the latest measured frame rate when performance testing is enabled."""
    if SHOW_FPS:
        cv2.putText(
            frame,
            f"FPS: {fps:.1f}",
            FPS_TEXT_POSITION,
            cv2.FONT_HERSHEY_SIMPLEX,
            FPS_TEXT_SCALE,
            FPS_TEXT_COLOR,
            FPS_TEXT_THICKNESS,
            cv2.LINE_AA,
        )


def draw_recording_indicator(frame) -> None:
    """Show recording status only on the preview after saving the frame."""
    cv2.putText(
        frame,
        REC_TEXT,
        REC_TEXT_POSITION,
        cv2.FONT_HERSHEY_SIMPLEX,
        REC_TEXT_SCALE,
        REC_TEXT_COLOR,
        REC_TEXT_THICKNESS,
        cv2.LINE_AA,
    )


def main() -> int:
    """Show the default webcam feed until the user presses Q."""
    try:
        suit_image = load_suit_image(SUIT_IMAGE_PATH)
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")
        return 1

    camera = cv2.VideoCapture(CAMERA_INDEX)
    if not camera.isOpened():
        print(
            "Error: Could not open the default webcam. Check that it is connected "
            "and not being used by another application."
        )
        return 1

    camera.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)

    pose_tracker = PoseTracker()
    background_replacer = BackgroundReplacer(BACKGROUND_IMAGE_PATH)
    background_enabled = (
        BACKGROUND_REPLACEMENT_ENABLED and background_replacer.is_available
    )
    if BACKGROUND_REPLACEMENT_ENABLED and not background_replacer.is_available:
        print(
            f"Warning: {background_replacer.error_message}. "
            "Using the normal webcam background."
        )

    suit_smoother = SuitSmoother(SMOOTHING_FACTOR)
    suit_visible = True
    resized_suit = None
    resized_suit_size = None
    fps = 0.0
    fps_frame_count = 0
    fps_start_time = time.perf_counter()
    recorder = Recorder(RECORDINGS_DIRECTORY)
    print("Suit image loaded. Webcam started. Press Q in the video window to quit.")

    try:
        while True:
            success, frame = camera.read()
            if not success or frame is None:
                print("Error: Could not read a frame from the webcam.")
                return 1

            if background_enabled:
                frame = background_replacer.replace_background(frame)

            pose_results = pose_tracker.detect_pose(frame)
            torso_points = pose_tracker.get_torso_points(pose_results, frame.shape)

            shoulder_measurements = get_shoulder_measurements(torso_points)
            if shoulder_measurements is not None:
                center_x, center_y, shoulder_width = suit_smoother.update(
                    *shoulder_measurements
                )
                suit_position = calculate_suit_position(
                    center_x,
                    center_y,
                    shoulder_width,
                    suit_image,
                    SUIT_LEFT_SHOULDER_X,
                    SUIT_RIGHT_SHOULDER_X,
                    SUIT_SHOULDER_Y,
                    SUIT_WIDTH_SCALE,
                    SUIT_HEIGHT_SCALE,
                    SUIT_X_OFFSET,
                    SUIT_Y_OFFSET,
                )
                suit_x, suit_y, suit_width, suit_height = suit_position
                suit_size = (suit_width, suit_height)
                if suit_size != resized_suit_size:
                    resized_suit = resize_suit(suit_image, *suit_size)
                    resized_suit_size = suit_size
                if suit_visible:
                    overlay_suit(frame, resized_suit, suit_x, suit_y)
            else:
                suit_smoother.reset()

            if SHOW_FPS:
                fps_frame_count += 1
                current_time = time.perf_counter()
                elapsed_time = current_time - fps_start_time
                if elapsed_time >= FPS_UPDATE_INTERVAL:
                    fps = fps_frame_count / elapsed_time
                    fps_frame_count = 0
                    fps_start_time = current_time
                draw_fps(frame, fps)

            if recorder.is_recording:
                recorder.write_frame(frame)

            preview_frame = frame.copy()
            if recorder.is_recording:
                draw_recording_indicator(preview_frame)

            cv2.imshow(WINDOW_TITLE, preview_frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("r"):
                if not recorder.is_recording:
                    try:
                        recording_path = recorder.start(frame)
                        print(f"Recording started: {recording_path}")
                    except RuntimeError as error:
                        print(f"Error: {error}")
                else:
                    recording_path = recorder.stop(frame)
                    if recording_path is not None:
                        print(f"Recording saved: {recording_path}")
            elif key == ord("b"):
                if background_replacer.is_available:
                    background_enabled = not background_enabled
                    status = "enabled" if background_enabled else "disabled"
                    print(f"Background replacement {status}.")
                else:
                    print("Background replacement is unavailable without assets/background.jpg.")
            elif key == ord("s"):
                suit_visible = not suit_visible
                status = "shown" if suit_visible else "hidden"
                print(f"Virtual suit {status}.")
            elif key == ord("q"):
                break
    finally:
        if recorder.is_recording:
            recording_path = recorder.stop(frame)
            if recording_path is not None:
                print(f"Recording saved: {recording_path}")
        background_replacer.close()
        pose_tracker.close()
        camera.release()
        cv2.destroyAllWindows()

    return 0


if __name__ == "__main__":
    sys.exit(main())
