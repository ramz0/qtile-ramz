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
  "groupbox": [
    widget.TextBox(
      fontsize=18,
      padding=2,
      background=colorBarraGrupos,
      **decor_left_soft,
    ),
    GroupBox(
      highlight_method="text",
      active=colorDeGruposActivos,
      this_current_screen_border=colorDelGrupoActual,
      fontsize=15,
      background=colorBarraGrupos,
      visible_groups=["1", "2", "3", "4", "5", "6"],
    ),
    widget.TextBox(
      fontsize=18,
      padding=2,
      background=colorBarraGrupos,
      **decor_right_soft,
    ),
  ],
  "groupbox_monitor": [
     widget.TextBox(
        fontsize=18,
        padding=2,
        background=colorBarraGrupos,
        **decor_left_soft,
    ),
    GroupBox(
        highlight_method="text",
        active=colorDeGruposActivos,
        this_current_screen_border=colorDelGrupoActual,
        fontsize=15,
        background=colorBarraGrupos,
        visible_groups=["1b", "2b", "3b", "4b", "5b", "6b"],
    ),
    widget.TextBox(
        fontsize=18,
        padding=2,
        background=colorBarraGrupos,
        **decor_right_soft,
    )
  ],
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