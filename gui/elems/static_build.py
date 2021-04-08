from common.html_builder.elem.option import *


def init():
    guitar_option = Option("guitar", elem_id="select_instrument_guitar", child_of="#instrument_selector_select")
    guitar_option.add_content("Guitar")
    guitar_option.build()

    piano_option = Option("piano", elem_id="select_instrument_piano", child_of="#instrument_selector_select")
    piano_option.add_content("Piano")
    piano_option.build()

    print("HTML Building finished")
