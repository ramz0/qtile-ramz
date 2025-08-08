from libqtile.config import Key
from libqtile.lazy import lazy
from shortcuts.config import mod, terminal


keys = [
    Key([mod], "space", lazy.window.toggle_floating()),

    Key([mod, "shift"], "Left", lazy.layout.left()),
    Key([mod, "shift"], "Right", lazy.layout.right()),
    Key([mod, "shift"], "Down", lazy.layout.down()),
    Key([mod, "shift"], "Up", lazy.layout.up()),

    Key([mod], "Left", lazy.layout.shuffle_left()),
    Key([mod], "Right", lazy.layout.shuffle_right()),
    Key([mod], "Down", lazy.layout.shuffle_down()),
    Key([mod], "Up", lazy.layout.shuffle_up()),

    Key([mod, "control"], "Left", lazy.layout.grow_left()),
    Key([mod, "control"], "Right", lazy.layout.grow_right()),
    Key([mod, "control"], "Down", lazy.layout.grow_down()),
    Key([mod, "control"], "Up", lazy.layout.grow_up()),
    Key([mod], "n", lazy.layout.normalize()),

    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Tab", lazy.next_layout()),

    Key([mod], "w", lazy.window.kill()),
    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "Return", lazy.spawn(terminal)),
]
