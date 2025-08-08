from libqtile.config import Key
from libqtile.lazy import lazy
from shortcuts.config import mod


keys = [
    Key([mod], "c", lazy.spawn("code")),
]