from qtile_extras.widget import decorations

decor_widget_round = {
    "decorations": [
        decorations.RectDecoration(
            filled=True,
            radius=10,
            use_widget_background=True,
        )
    ],
}

decor_left_edge = {
    "decorations": [
        decorations.RectDecoration(
            filled=True,
            radius=[4, 0, 0, 10],
            use_widget_background=True,
        )
    ],
}

decor_right_edge = {
    "decorations": [
        decorations.RectDecoration(
            filled=True,
            radius=[0, 10, 4, 0],
            use_widget_background=True,
        )
    ],
}

decor_left_soft = {
    "decorations": [
        decorations.RectDecoration(
            filled=True,
            radius=[10, 0, 0, 10],
            use_widget_background=True,
        )
    ],
}

decor_right_soft = {
    "decorations": [
        decorations.RectDecoration(
            filled=True,
            radius=[0, 10, 10, 0],
            use_widget_background=True,
        )
    ],
}
