from libqtile import widget
from libqtile.lazy import lazy

from personalWidgets.battery import BatteryIcon
from personalWidgets.windowName import MinimalistWindowName
from personalWidgets.groupBox import GroupBox

# Decoraciones
from theme.colors import *
from bar.visuals.decorations import *

widgets = {
  "softwarename": MinimalistWindowName(
    foreground = colorDeTextos,
  ),
  "groupbox": GroupBox(
    highlight_method="text",
    active=colorDeGruposActivos,
    this_current_screen_border=colorDelGrupoActual,
    fontsize=15,
  ),
  "battery": [
    BatteryIcon(
      update_interval=30,
      format="{icon}",
      fontsize=13,
      padding=6,
      background=colorBateria,
      foreground=colorBarra,
      **decoration_left,
    ),
    widget.Battery(
      charge_char = '',
      discharge_char="",
      update_interval=30,
      format="{percent:2.0%}  {char}",
      padding=8,
      background=colorBateria,
      foreground=colorBarra,
      **decoration_rigth,
    ),
  ]
}