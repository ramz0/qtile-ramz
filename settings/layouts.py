from libqtile import layout

from theme.colors import border_focus

Modlayouts = [
    layout.MonadTall(
        border_focus=border_focus,
        single_border_width=0,
        margin=8,
        single_margin=8,
        border_width=2,
        border_radius= 12,
    ),
    layout.Max(
        margin=10,
        single_margin=10,
    ),
]