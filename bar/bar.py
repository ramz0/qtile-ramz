import os
from libqtile import bar
from libqtile.config import Screen

from theme.colors import *

from bar.widgets import widgets

bar_widgets = [
    widgets["launcher"],
    widgets["big_spacer"],
    *widgets["groupbox"],
    widgets["big_spacer"],
    widgets["sep"],
    widgets["softwarename"],
    widgets["prompt"],
    widgets["small_spacer"],
    widgets["systray"],
    widgets["small_spacer"],
    widgets["updates"],
    widgets["sep"],
    *widgets["volume"],
    widgets["small_spacer"],
    *widgets["backlight"],
    widgets["small_spacer"],
    *widgets["battery"],
    widgets["small_spacer"],
    *widgets["clock"],
]

# Creacion de la Barra del sistema.
bar = [
    Screen(
        wallpaper=os.path.expanduser("~/Documents/wallpapers/street.jpg"),
        # Podemos cambiar a [top, bottom].
        top=bar.Bar(
            bar_widgets,
            21,
            margin=[5, 5, 0, 5],
            background=colorBarra,
            border_width=4,  # Draw top and bottom borders
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