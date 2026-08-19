"""Simple smoothing for the suit's shoulder-based measurements."""


class SuitSmoother:
    """Apply exponential smoothing to position and shoulder width."""

    def __init__(self, factor: float) -> None:
        if not 0 < factor <= 1:
            raise ValueError("Smoothing factor must be greater than 0 and at most 1.")

        self.factor = factor
        self._center_x = None
        self._center_y = None
        self._shoulder_width = None

    def update(
        self, center_x: float, center_y: float, shoulder_width: float
    ) -> tuple[float, float, float]:
        """Return the latest smoothed shoulder measurements."""
        if self._center_x is None:
            self._center_x = center_x
            self._center_y = center_y
            self._shoulder_width = shoulder_width
        else:
            self._center_x = self._smooth(self._center_x, center_x)
            self._center_y = self._smooth(self._center_y, center_y)
            self._shoulder_width = self._smooth(self._shoulder_width, shoulder_width)

        return self._center_x, self._center_y, self._shoulder_width

    def reset(self) -> None:
        """Forget old measurements after the shoulders leave the frame."""
        self._center_x = None
        self._center_y = None
        self._shoulder_width = None

    def _smooth(self, previous: float, current: float) -> float:
        return previous * (1 - self.factor) + current * self.factor
