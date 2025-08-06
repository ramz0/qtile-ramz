from libqtile.config import Key 
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

llaves = [
    
    # [Hacer/Desacer] una ventana Flotante.
    Key([mod], "space", lazy.window.toggle_floating()),
  
    # Cambiamos entre el foco de las ventanas.
    Key([mod, "shift"], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod, "shift"], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod, "shift"], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod, "shift"], "Up", lazy.layout.up(), desc="Move focus up"),
    
    # Mover ventanas.
    Key([mod], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #  ~ Rofi.
    Key(
        [mod],
        "r",
        lazy.spawn('rofi -show drun -icon-theme "Papirus" -show-icons'),
        desc="Menu de ~Rofi",
    ),
    Key(
        ["mod1"], "Tab",
        lazy.spawn('rofi -show window -icon-theme "Papirus" -show-icons'),
        desc="Cambiar a la siguiente ventana en Rofi"
    ),
    Key(
        [mod],
        "e",
        lazy.spawn("rofi -show emoji"),
        desc="Spawn a command using a prompt ~Rofi Emojis",
    ),
    Key(
        [mod],
        "p",
        lazy.spawn(".config/rofi/bin/powermenu"),
        desc="Spawn a command usung ~Rofi PowerMenu",
    ),

    #  Abrir VSCode.
    Key([mod], "c", lazy.spawn("code"), desc="Open visual-studio-code"),
    
    # Volumen
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 2")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 2")),

    # Brillo
    Key([mod], "i", lazy.spawn("brightnessctl set +5%"), desc="Aumentar brillo"),
    Key([mod], "k", lazy.spawn("brightnessctl set 5%-"), desc="Disminuir brillo"),
     
    # Reproducción de medios
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
]