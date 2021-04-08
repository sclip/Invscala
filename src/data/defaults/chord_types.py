class ChordTypes:
    __chord_types = {}

    def get_chord_types(self):
        return self.__chord_types

    def set_chord_types(self, to_set_list):
        for chord_type_name in to_set_list:
            self.__chord_types.setdefault(chord_type_name, to_set_list[chord_type_name])


chord_types = ChordTypes()
