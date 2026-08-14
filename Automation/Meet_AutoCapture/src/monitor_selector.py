"""Physical-monitor discovery and terminal selection."""

import os
import msvcrt
from dataclasses import dataclass

import mss


@dataclass(frozen=True)
class Monitor:
    """One physical display reported by MSS."""

    index: int
    bounds: dict[str, int]
    is_primary: bool

    @property
    def label(self) -> str:
        primary_text = " (Primary)" if self.is_primary else ""
        return (
            f"Display {self.index}{primary_text} - "
            f"{self.bounds['width']}x{self.bounds['height']}"
        )


def list_monitors() -> list[Monitor]:
    """Return physical monitors individually, excluding MSS's combined desktop."""
    with mss.mss() as screen_capture:
        monitors = screen_capture.monitors[1:]

    # MSS lists the primary display first on Windows.
    return [
        Monitor(index=index, bounds=dict(bounds), is_primary=index == 1)
        for index, bounds in enumerate(monitors, start=1)
    ]


def select_monitor() -> Monitor | None:
    """Automatically select one display, or show a terminal picker for several."""
    monitors = list_monitors()
    if not monitors:
        print("No physical displays are available to capture.")
        return None

    if len(monitors) == 1:
        monitor = monitors[0]
        print(f"Using {monitor.label}")
        print("Monitoring started.")
        return monitor

    selected_index = 0
    while True:
        os.system("cls")
        print("Select monitor to capture:\n")
        for index, monitor in enumerate(monitors):
            marker = ">" if index == selected_index else " "
            print(f"{marker} {monitor.label}")
        print("\nUp/Down Select   Enter Confirm   Ctrl+C Cancel")

        key = msvcrt.getwch()
        if key in ("\x00", "\xe0"):
            key = msvcrt.getwch()
            if key == "H":
                selected_index = (selected_index - 1) % len(monitors)
            elif key == "P":
                selected_index = (selected_index + 1) % len(monitors)
        elif key == "\r":
            os.system("cls")
            return monitors[selected_index]
