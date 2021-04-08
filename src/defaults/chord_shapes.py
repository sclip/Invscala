class ChordShapes:
    __chord_shapes = {}

    def get_chord_shapes(self):
        return self.__chord_shapes

    def set_chord_shapes(self, to_set_list):
        for chord_shape_name in to_set_list:
            self.__chord_shapes.setdefault(chord_shape_name, to_set_list[chord_shape_name])


chord_shapes = ChordShapes()
