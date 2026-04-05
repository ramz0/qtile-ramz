import subprocess
from libqtile.config import Key
from libqtile.lazy import lazy
from shortcuts.config import mod


def toggle_hdmi(qtile):
    result = subprocess.run(["xrandr"], capture_output=True, text=True)
    if "HDMI-1 connected" in result.stdout:
        subprocess.run([
            "xrandr",
            "--output", "eDP-1", "--auto", "--primary",
            "--output", "HDMI-1", "--mode", "1920x1080", "--right-of", "eDP-1",
        ])
    else:
        subprocess.run([
            "xrandr",
            "--output", "HDMI-1", "--off",
            "--output", "eDP-1", "--auto",
        ])
    qtile.reconfigure_screens()


def toggle_laptop_bar(qtile):
    qtile.hide_show_bar_screen(qtile.screens[0])


def toggle_monitor_bar(qtile):
    if len(qtile.screens) > 1:
        qtile.hide_show_bar_screen(qtile.screens[1])


keys = [
    Key([mod], "m",
        lazy.function(toggle_hdmi),
        desc="Toggle HDMI-1 a la derecha"),
    Key([mod], "b",
        lazy.function(toggle_laptop_bar),
        desc="Mostrar/ocultar barra de la laptop"),
    Key([mod, "shift"], "b",
        lazy.function(toggle_monitor_bar),
        desc="Mostrar/ocultar barra del monitor externo"),
]
