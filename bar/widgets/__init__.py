from bar.widgets.basics import widgets as basic_widgets
from bar.widgets.customs import widgets as custom_widgets
from bar.widgets.blocks import blocks as widgets_blocks

widgets = {
    **basic_widgets,
    **custom_widgets,
    **widgets_blocks,
}