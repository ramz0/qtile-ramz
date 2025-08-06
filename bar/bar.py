import os
from libqtile import bar, widget
from qtile_extras import widget
from libqtile.config import Screen
from personalWidgets import battery, groupBox, windowName
from libqtile.widget.backlight import Backlight
from libqtile.lazy import lazy
from coloresWidgets import *

from bar.visuals.decorations import *

from bar.widgets import widgets

bar_widgets = [
    widgets["launcher"],
    widgets["prompt"],
    widgets["systray"],
    widgets["updates"],
    *widgets["volume"],
    *widgets["backlight"],
    *widgets["clock"],
]

# Creacion de la Barra del sistema.
bar = [
    Screen(
        wallpaper=os.path.expanduser("~/documents/wallpapers/street.jpg"),
        # bottom=bar.Bar(
        top=bar.Bar(
            bar_widgets,
            21,
            margin=[10, 10, 0, 10],
            background=colorBarra,
            border_width=3,  # Draw top and bottom borders
            border_color=colorBarra,  # Borders are magenta
        ),
    ),
]

# cofiguracion general de los widgets.
widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)

widget_defaults = widget_defaults.copy()