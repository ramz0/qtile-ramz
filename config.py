import sys

# Forzar instancias frescas de widgets en cada reload_config()
# Sin esto, Python reutiliza los mismos objetos de widgets cacheados
# causando que la barra antigua y la nueva compartan instancias.
_mods_bar = [m for m in list(sys.modules) if m.startswith("bar") or m.startswith("theme")]
for _m in _mods_bar:
    del sys.modules[_m]

from libqtile import layout
from libqtile.config import Match

from bar.bar import bar
from bar.bar import widget_defaults

from shortcuts import keys
from shortcuts.mouse import accionesRaton

from settings.groups import grupos 
from settings.layouts import Modlayouts


# Cargar configuracion de Comandos de Teclado.
keys = keys

# Cargar grupos de la barra del sistema.
groups = grupos

# Cargar la Configuracion de layouts
layouts = Modlayouts

# Cargar la configuracion general de Todos los widgets.
extension_defaults = widget_defaults

# Cargar la Barra del sistema.
screens = bar

# Acciones y comandos del raton
mouse = accionesRaton

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus="#ab9df2",
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
)


auto_fullscreen = True
auto_minimize = False
focus_on_window_activation = "smart"
reconfigure_screens = True
wmname = "qtile"