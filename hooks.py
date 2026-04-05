import subprocess
from libqtile import hook, qtile

PAIRED_GROUPS = {
    "1b": "1",
    "2b": "2",
    "3b": "3",
    "4b": "4",
    "5b": "5",
    "6b": "6",
}


def _rescue_secondary_windows():
    """Mueve todas las ventanas de grupos secundarios al grupo primario correspondiente."""
    for secondary, primary in PAIRED_GROUPS.items():
        group = qtile.groups_map.get(secondary)
        if group:
            for window in list(group.windows):
                window.togroup(primary)


@hook.subscribe.screen_change
def auto_monitor(event):
    """
    Se dispara cuando cambia la configuración de pantallas (conectar/desconectar HDMI).
    Si HDMI-1 está conectado, lo activa a la derecha de eDP-1 a 1920x1080.
    Si no está conectado, rescata las ventanas del monitor y lo apaga.
    """
    if qtile is None:
        return

    result = subprocess.run(["xrandr"], capture_output=True, text=True)

    if "HDMI-1 connected" in result.stdout:
        subprocess.run([
            "xrandr",
            "--output", "eDP-1", "--auto", "--primary",
            "--output", "HDMI-1", "--mode", "1920x1080", "--right-of", "eDP-1",
        ])
    else:
        # Primero rescatar ventanas antes de que el monitor desaparezca
        _rescue_secondary_windows()
        subprocess.run([
            "xrandr",
            "--output", "HDMI-1", "--off",
            "--output", "eDP-1", "--auto",
        ])

    qtile.reconfigure_screens()
