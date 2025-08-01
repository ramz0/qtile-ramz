from libqtile.config import  Group, Key
from libqtile.lazy import lazy
from shortcuts.keys import llaves, mod

keys = llaves

grupos = [Group(i) for i in ["1", "2", "3", "4", "5", "6"]]

# 󰡙 󰡘 󰡜 󰡗 󰡚 󰡛      綠  祿     󱓞 󰫣     󰇧    ⏾    󰧞 󰧟 󰆘 󰷀

for i, group in enumerate(grupos):
    print('index: ', i, ' grupo: ', group, ' Nombre del grupo: ', group.name)
    index = str(i + 1)
    keys.extend(
        [
            Key(
                [mod],
                index,
                lazy.group[group.name].toscreen(toggle=True),
                desc="Switch to groups {}".format(group.name),
            ),
            Key(
                [mod, "shift"],
                index,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to groups {}".format(group.name),
            ),
        ]
    )