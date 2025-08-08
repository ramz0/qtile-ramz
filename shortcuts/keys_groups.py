from libqtile.config import Key
from libqtile.lazy import lazy

from settings.groups import grupos  
from shortcuts.config import mod

keys = []

for i, group in enumerate(grupos):
    index = str(i + 1)
    keys.extend([
        Key(
            [mod],
            index,
            lazy.group[group.name].toscreen(toggle=True),
            desc=f"Switch to group {group.name}",
        ),
        Key(
            [mod, "shift"],
            index,
            lazy.window.togroup(group.name, switch_group=True),
            desc=f"Switch to & move focused window to group {group.name}",
        ),
    ])
