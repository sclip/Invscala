import music21


class Octave:
    __octave = music21.stream.Stream()  # One of each

    def set_octave(self, notes_):
        for note in notes_:
            self.__octave.append(note)

    def get_octave(self):
        return self.__octave


octave = Octave()
