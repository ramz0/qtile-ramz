import os
from libqtile import bar, widget
from qtile_extras import widget
from libqtile.config import Screen
from personalWidgets import battery, groupBox, windowName
from libqtile.widget.backlight import Backlight
from libqtile.lazy import lazy
from coloresWidgets import *

from bar.visuals.decorations import *

# Creacion de la Barra del sistema.
bar = [
    Screen(
        wallpaper=os.path.expanduser("~/documents/wallpapers/street.jpg"),
        # bottom=bar.Bar(
        top=bar.Bar(
            [
                widget.TextBox(
                    text="",
                    background=colorMenuRofi,
                    foreground=colorBarra,
                    padding=16,
                    fontsize=19,
                    **decoration_left,
                    mouse_callbacks={
                        "Button1": lazy.spawn(
                            'rofi -show drun -icon-theme "Papirus" -show-icons'
                        ),
                    },
                ),
                widget.TextBox(padding=2, background=colorMenuRofi, **decoration_rigth),

                widget.Sep(padding=13),

                groupBox.GroupBox(
                    highlight_method="text",
                    active=colorDeGruposActivos,
                    this_current_screen_border=colorDelGrupoActual,
                    fontsize=15,
                ),

                widget.Sep(padding=13),
                # widget.CurrentLayout(),
                widget.Prompt(),

                windowName.MinimalistWindowName(
                  foreground = colorDeTextos,
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.StatusNotifier(),
                widget.Systray(icon_size=17),
                widget.Spacer(length=5),
                widget.CheckUpdates(
                    display_format="󰻌",
                    no_update_string="󰕥",
                    colour_have_updates=colorIndicadorDeActualizaciones,
                    colour_no_updates=colorIndicadorDeActualizaciones,
                    fontsize=18,
                ),
                widget.Sep(padding=13),
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
                widget.Spacer(length=5),
                widget.TextBox(
                    text="",
                    fontsize=17,
                    padding=8,
                    foreground=colorBarra,
                    background=colorBrillo,
                    **decoration_left,
                ),
                Backlight(
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
                widget.Spacer(length=5),
                battery.BatteryIcon(
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
                widget.Spacer(length=5),
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
                    **decoration_rigth,
                ),
            ],
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