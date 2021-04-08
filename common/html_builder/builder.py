import eel


class HTMLBuilder:
    @staticmethod
    def build(elem, to):
        """
        Append this element to another
        :param elem: Element to append
        :param to: ID or class of the element to append to
        """
        if str(to)[0] == "#":
            new_to = ""
            for ltr in to:
                if ltr != to[0]:
                    new_to += ltr
            eel.build_elem(elem, new_to)
        elif str(to)[0] == ".":
            new_to = ""
            for ltr in to:
                if ltr != to[0]:
                    new_to += ltr
            eel.build_elems(elem, new_to)
