from enum import Enum, unique
from typing import NamedTuple
from libqtile.widget import battery

@unique
class BatteryState(Enum):
    CHARGING = 1
    DISCHARGING = 2
    FULL = 3
    EMPTY = 4
    UNKNOWN = 5

BatteryStatus = NamedTuple(
    "BatteryStatus",
    [
        ("state", BatteryState),
        ("percent", float),
        ("power", float),
        ("time", int),
    ],
)

class BatteryIcon(battery.Battery):

  def build_string(self, status: BatteryStatus) -> str:
    """Determine the string to return for the given battery state
    Parameters
    ----------
    status:
      The current status of the battery
    Returns
    -------
    str
      The string to display for the current status.
    """
    if self.hide_threshold is not None and status.percent > self.hide_threshold:
      return ""

    if self.layout is not None:
      if status.state == BatteryState.DISCHARGING and status.percent < self.low_percentage:
        self.layout.colour = self.low_foreground
        self.background = self.low_background
      else:
        self.layout.colour = self.foreground
        self.background = self.normal_background

    if status.state == BatteryState.CHARGING:
      char = self.charge_char
    elif status.state == BatteryState.DISCHARGING:
      char = self.discharge_char
    elif status.state == BatteryState.FULL:
      if self.show_short_text:
        return "Full"
      char = self.full_char
    elif status.state == BatteryState.EMPTY or (
      status.state == BatteryState.UNKNOWN and status.percent == 0
    ):
      if self.show_short_text:
        return "Empty"
      char = self.empty_char
    else:
      char = self.unknown_char

    hour = status.time // 3600
    minute = (status.time // 60) % 60

    # /////////
    icon = "None"
    percent = status.percent

    batteryIcon = {
      0.80 : "",
      0.60 : "", 
      0.40 : "", 
      0.05 : "", 
      0.00 : ""
    }

    for index, value in batteryIcon.items():
      if (percent >= index):
        icon = value
        break

    # ///////////

    return self.format.format(
      char=char, percent=status.percent, watt=status.power, hour=hour, min=minute, icon = icon
    )