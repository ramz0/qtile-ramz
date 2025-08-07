from qtile_extras.widget import decorations

decoration_round = {
    "decorations": [
        decorations.RectDecoration(
            filled=True,
            radius=10,
            use_widget_background=True,
        )
    ],
}

decoration_left = {
    "decorations": [
        decorations.RectDecoration(
            filled=True,
            radius=[4, 0, 0, 10],
            use_widget_background=True,
        )
    ],
}

decoration_rigth = {
    "decorations": [
        decorations.RectDecoration(
            filled=True,
            radius=[0, 10, 4, 0],
            use_widget_background=True,
        )
    ],
}

decoration_rigth2 = {
    "decorations": [
        decorations.RectDecoration(
            filled=True,
            radius=[0, 10, 10, 0],
            use_widget_background=True,
        )
    ],
}
