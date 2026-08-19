"""MediaPipe pose tracking for the user's torso landmarks."""

import cv2
import mediapipe as mp


LANDMARK_NAMES = {
    "left_shoulder": mp.solutions.pose.PoseLandmark.LEFT_SHOULDER,
    "right_shoulder": mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER,
    "left_hip": mp.solutions.pose.PoseLandmark.LEFT_HIP,
    "right_hip": mp.solutions.pose.PoseLandmark.RIGHT_HIP,
}
MIN_VISIBILITY = 0.5


class PoseTracker:
    """Detect the shoulders and hips in webcam frames."""

    def __init__(self) -> None:
        self._pose = mp.solutions.pose.Pose(
            static_image_mode=False,
            model_complexity=1,
            smooth_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        )

    def detect_pose(self, frame):
        """Return MediaPipe pose results for one BGR webcam frame."""
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self._pose.process(rgb_frame)

    def get_torso_points(self, pose_results, frame_shape) -> dict[str, tuple[int, int]]:
        """Return visible shoulder and hip points as pixel coordinates."""
        if not pose_results.pose_landmarks:
            return {}

        frame_height, frame_width = frame_shape[:2]
        points = {}

        for name, landmark_index in LANDMARK_NAMES.items():
            landmark = pose_results.pose_landmarks.landmark[landmark_index]
            if landmark.visibility < MIN_VISIBILITY:
                continue

            points[name] = (
                int(landmark.x * frame_width),
                int(landmark.y * frame_height),
            )

        return points

    def close(self) -> None:
        """Release MediaPipe resources when the app exits."""
        self._pose.close()
