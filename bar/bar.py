import os
from libqtile import bar
from libqtile.config import Screen

from theme.colors import *
from theme.decorations import *

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
    *widgets["clock"]
]

bar_widgets_secondary = [
    widgets["small_spacer"],
    *widgets["groupbox_monitor"],
    widgets["sep"],
    widgets["softwarename"],
    widgets["sep"],
    *widgets["cpu_state"],
    widgets["big_spacer"],
    *widgets["clock"],
]

# Creacion de la Barra del sistema.
bar = [
    Screen(
        wallpaper=os.path.expanduser("~/documents/wallpapers/starwars.png"),
        top=bar.Bar(
            bar_widgets,
            20,
            margin=[3, 3, 0, 3],
            background=colorBarra,
            border_width=4,
            border_color=colorBarra,
        ),
    ),
    Screen(
        wallpaper=os.path.expanduser("~/documents/wallpapers/starwars_m.png"),
        top=bar.Bar(
            bar_widgets_secondary,
            20,
            margin=[3, 3, 0, 3],
            background=colorBarra,
            border_width=4,
            border_color=colorBarra,
        ),
    ),
]

# cofiguracion general de los widgets.
widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=4,
)

widget_defaults = widget_defaults.copy()
