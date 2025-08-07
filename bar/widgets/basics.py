from libqtile import widget
from libqtile.lazy import lazy

# Decoraciones
from coloresWidgets import *
from bar.visuals.decorations import *

widgets = {
    "launcher": widget.TextBox(
        text="󰣇",
        background=colorMenuRofi,
        foreground=colorBarra,
        padding=23,
        fontsize=19,
        **decoration_round,
        mouse_callbacks={
            "Button1": lazy.spawn(
                'rofi -show drun -icon-theme "Papirus" -show-icons'
            ),
        },
    ),
    "prompt": widget.Prompt(),
    "systray": widget.Systray(icon_size=17),
    "updates": widget.CheckUpdates(
        display_format="󰻌",
        no_update_string="󰕥",
        colour_have_updates=colorIndicadorDeActualizaciones,
        colour_no_updates=colorIndicadorDeActualizaciones,
        fontsize=18,
    ),
    "volume":[
        widget.TextBox(
            text="󰕾",
            fontsize=16,
            padding=8,
            foreground=colorBarra,
            background=colorVolumen,
            **decoration_left,
        ),
        widget.Volume(
            foreground=colorBarra,
            background=colorVolumen,
            padding=8,
            **decoration_rigth,
        ),
    ],
    "backlight":[
        widget.TextBox(
            text="",
            fontsize=17,
            padding=8,
            foreground=colorBarra,
            background=colorBrillo,
            **decoration_left,
        ),
        widget.Backlight(
            backlight_name="intel_backlight",
            padding=8,
            foreground=colorBarra,
            background=colorBrillo,
            **decoration_rigth,
        ),
        widget.TextBox(
            background=colorBrillo,
            **decoration_rigth,
        ),
    ],
    "clock": [
        widget.TextBox(
            text="",
            fontsize=14,
            padding=6,
            background=colorFechaYHora,
            foreground=colorBarra,
            **decoration_left,
        ),
        widget.Clock(
            format="%I:%M %p",
            padding=8,
            background=colorFechaYHora,
            foreground=colorBarra,
        ),
        widget.TextBox(
            text="",
            fontsize=14,
            padding=6,
            background=colorFechaYHora,
            foreground=colorBarra,
        ),
        widget.Clock(
            format="%Y-%m-%d",
            background=colorFechaYHora,
            foreground=colorBarra,
            padding=8,
            **decoration_rigth2,
        ),
    ]
}
