from common.html_builder.elem import div, option


def build_fret_numbering(frets):
    for i in range(int(frets)):
        new_elem = div.Div(elem_class="fret_marker", child_of="#fret_n")
        new_elem.add_content(str(i))
        new_elem.build()


def build_string(strings):
    for i in range(strings):
        new_elem = div.Div(elem_id=f"string{i}", elem_class="string", child_of="#strings")
        new_elem.add_content("<hr class='string_graphic'>")
        new_elem.build()


def build_frets(frets, string, string_id):
    nut_fret = div.Div(elem_id=f"fret{string.get_fret(0).get_name()}", elem_class="nut_fret", child_of=f"#string{string_id}")
    nut_fret.add_content(f"<div id='fret{string.get_fret(0).get_name()}_name' class='fret_name'>{str(string.get_fret(0).get_note().name).replace('-', 'b')}</div>")
    nut_fret.build()
    for i in range(1, int(frets)):
        new_fret = div.Div(elem_id=f"fret{string.get_fret(i).get_name()}", elem_class="fret", child_of=f"#string{string_id}")
        new_fret.add_content(f"<div id='fret{string.get_fret(i).get_name()}_name' class='fret_name'>{str(string.get_fret(i).get_note().name).replace('-', 'b')}</div>")
        # new_fret.add_content(f"<div id='fret{string.get_fret(i).get_name()}_name' class='fret_name'>{str(string.get_fret(i).get_note().name).replace('-', 'b')}</div>")
        # ^ above should be for numbers
        new_fret.build()


def build_string_selection(strings_min, strings_max, strings_count):
    for i in range(strings_min, strings_max + 1):
        if i == strings_count:
            new_option = option.Option(f"{i}", child_of="#string_count_select", attr=["selected"])
        else:
            new_option = option.Option(f"{i}", child_of="#string_count_select")
        new_option.add_content(f"{i}")
        new_option.build()
