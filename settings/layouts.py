from libqtile import layout

Modlayouts = [
    layout.MonadTall(
        border_focus="#ab9df2",
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