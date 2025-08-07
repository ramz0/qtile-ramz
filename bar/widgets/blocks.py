from libqtile import widget


# Espaciadores invisibles (espacio en blanco entre bloques)
blocks = {
  "sep": widget.Sep(padding=13),  
  "small_sep": widget.Sep(padding=6),
  "big_sep": widget.Sep(padding=20),

  "small_spacer": widget.Spacer(length=5),
  "big_spacer": widget.Spacer(length=15),
}