from libqtile.config import Key
from libqtile.lazy import lazy
from shortcuts.config import mod


keys = [
    Key([mod], "r", lazy.spawn('rofi -show drun -icon-theme "Papirus" -show-icons')),
    Key(["mod1"], "Tab", lazy.spawn('rofi -show window -icon-theme "Papirus" -show-icons')),
    Key([mod], "e", lazy.spawn("rofi -show emoji")),
    Key([mod], "p", lazy.spawn(".config/rofi/bin/powermenu")),
    Key(["control", "shift"], "s", lazy.spawn(".config/rofi/bin/screenshot")),
    Key([mod], "d", lazy.spawn(".config/rofi/bin/calendar")),
    Key([mod, "shift"], "n", lazy.spawn(".config/rofi/bin/wifi")),
]
