from common.html_builder import element


class Select(element.Element):
    def __init__(self, elem_id, elem_class="", child_of=""):
        super().__init__("select", elem_id=elem_id, elem_class=elem_class, attr=[f'name="{elem_id}"'], child_of=child_of)
