from common.html_builder import builder


class Element:
    def __init__(self, name, elem_id="", elem_class="", attr=None, child_of="", testing=False):

        if attr is None:
            self.__attr_list = []
        else:
            self.__attr_list = attr

        if attr is None:
            self.__attr = ""
        else:
            self.__attr = " " + str(" ".join(self.__attr_list))

        self.__elem_id = elem_id
        self.__elem_class = elem_class

        if elem_id != "":
            self.__elem_id = f' id="{elem_id}"'
        if elem_class != "":
            self.__elem_class = f' class="{elem_class}"'

        self.__elem_name = name
        self.__start_tag = f"<{self.__elem_name}{self.__elem_id}{self.__elem_class}{self.__attr}>"
        self.__end_tag = f"</{self.__elem_name}>"

        self.__content = ""
        self.__child_of = child_of

        self.__full_tag = f"{self.__start_tag}{self.__content}{self.__end_tag}"
        self._update_tag()

    def get_element(self):
        return self.__full_tag

    def add_content(self, content):
        self.__content += str(content)
        self._update_tag()

    def _add_attr(self, attr):
        self.__attr_list.append(attr)
        self.__attr = " " + str(" ".join(self.__attr_list))
        self._update_tag()

    def _update_tag(self):
        self.__full_tag = f"{self.__start_tag}{self.__content}{self.__end_tag}"

    def build(self):
        builder.HTMLBuilder.build(self.get_element(), self.__child_of)
