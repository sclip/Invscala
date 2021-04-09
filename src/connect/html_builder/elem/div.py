from src.connect.html_builder import element


class Div(element.Element):
    def __init__(self, elem_id="", elem_class="", child_of=""):
        super().__init__("div", elem_id=elem_id, elem_class=elem_class, child_of=child_of)
