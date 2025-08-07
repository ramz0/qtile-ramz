from libqtile import layout
from libqtile.config import Match

from bar.bar import bar
from bar.bar import widget_defaults

from shortcuts.keys import llaves
from shortcuts.mouse import accionesRaton

from settings.escritorios import grupos 
from settings.layouts import Modlayouts


# Cargar configuracion de Comandos de Teclado.
keys = llaves

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