import music21


class Notes:
    __notes = music21.stream.Stream()  # Repeating set

    def set_notes(self, notes_):
        for note in notes_:
            self.__notes.append(note)

    def get_notes(self):
        return self.__notes


notes = Notes()
