from libqtile.config import Key
from libqtile.lazy import lazy
from shortcuts.config import mod


keys = [
    # Volumen
    Key([], "XF86AudioMute", lazy.spawn(".config/rofi/bin/volume-bar toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn(".config/rofi/bin/volume-bar down")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(".config/rofi/bin/volume-bar up")),

    # Brillo
    Key([mod], "i", lazy.spawn("brightnessctl set +5%")),
    Key([mod], "k", lazy.spawn("brightnessctl set 5%-")),

    # Reproducción
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
]
