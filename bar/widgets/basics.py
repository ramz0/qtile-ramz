from libqtile import widget
from qtile_extras import widget
from libqtile.lazy import lazy

# Decoraciones
from theme.colors import *
from theme.decorations import *

widgets = {
    "launcher": widget.TextBox(
        text="󰣇",
        background=colorMenuRofi,
        foreground=colorBarra,
        padding=23,
        fontsize=19,
        **decor_widget_round,
        mouse_callbacks={
            "Button1": lazy.spawn(
                'rofi -show drun -icon-theme "Papirus" -show-icons'
            ),
        },
    ),
    "prompt": widget.Prompt(),
    "systray": widget.Systray(
      icon_size=17, 
      foreground=colorBarra,
      background=colorBarra
    ),
    "statusnotifier": widget.StatusNotifier(icon_size=17, padding=4),
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
            **decor_left_edge,
        ),
        widget.Volume(
            foreground=colorBarra,
            background=colorVolumen,
            padding=8,
            **decor_right_edge,
        ),
    ],
    "backlight":[
        widget.TextBox(
            text="",
            fontsize=17,
            padding=8,
            foreground=colorBarra,
            background=colorBrillo,
            **decor_left_edge,
        ),
        widget.Backlight(
            backlight_name="intel_backlight",
            padding=8,
            foreground=colorBarra,
            background=colorBrillo,
            **decor_right_edge,
        ),
    ],
    "clock": [
        widget.TextBox(
            text="",
            fontsize=14,
            padding=6,
            background=colorFechaYHora,
            foreground=colorBarra,
            **decor_left_edge,
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
            **decor_right_soft,
        ),
    ],
    "cpu_state":[
        widget.TextBox(
            text="",
            fontsize=14,
            padding=8,
            foreground=colorBarra,
            background=colorCPU,
            **decor_left_edge,
        ),
        widget.CPU(
          padding=10,
          foreground=colorBarra,
          background=colorCPU,
          **decor_right_edge
        ),
    ],
}
