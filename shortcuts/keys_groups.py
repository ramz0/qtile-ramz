from libqtile.config import Key
from libqtile.lazy import lazy

from settings.groups import primary_groups
from shortcuts.config import mod


def go_to_workspace(name):
    paired = name + "b"
    def _inner(qtile):
        screen0 = qtile.screens[0]
        if screen0.group.name == name:
            # Toggle: cada pantalla vuelve a su grupo anterior
            if screen0.previous_group:
                screen0.set_group(screen0.previous_group)
            if len(qtile.screens) > 1:
                screen1 = qtile.screens[1]
                if screen1.previous_group:
                    screen1.set_group(screen1.previous_group)
        else:
            # Cambio normal: ambas pantallas van al escritorio N
            if len(qtile.screens) > 1:
                qtile.groups_map[paired].toscreen(1)
            screen0.set_group(qtile.groups_map[name])
    return _inner


def move_window_to_workspace(name):
    paired = name + "b"
    def _inner(qtile):
        if qtile.current_window:
            qtile.current_window.togroup(name)
        if len(qtile.screens) > 1:
            qtile.groups_map[paired].toscreen(1)
        qtile.groups_map[name].toscreen(0)
    return _inner


keys = []

for name in primary_groups:
    keys.extend([
        Key(
            [mod],
            name,
            lazy.function(go_to_workspace(name)),
            desc=f"Ir al escritorio {name}",
        ),
        Key(
            [mod, "shift"],
            name,
            lazy.function(move_window_to_workspace(name)),
            desc=f"Mover ventana al escritorio {name}",
        ),
    ])
