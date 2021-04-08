from common.html_builder import element


class Option(element.Element):
    def __init__(self, value, elem_id="", elem_class="", child_of="", attr=None):
        super().__init__("option", elem_id=elem_id, elem_class=elem_class, child_of=child_of, attr=attr)
        if value != "":
            self.__elem_id = f' id="{value}"'

        self._add_attr(f'value="{value}"')
