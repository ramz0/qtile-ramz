from libqtile import widget
from qtile_extras import widget
from libqtile.lazy import lazy

from bar.widgets.extensions.battery import BatteryIcon
from bar.widgets.extensions.windowName import MinimalistWindowName
from bar.widgets.extensions.groupBox import GroupBox

# Decoraciones
from theme.colors import *
from theme.decorations import *

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
      **decor_left_edge,
    ),
    widget.Battery(
      charge_char = '',
      discharge_char="",
      update_interval=30,
      format="{percent:2.0%}  {char}",
      padding=8,
      background=colorBateria,
      foreground=colorBarra,
      **decor_right_edge,
    ),
  ]
}