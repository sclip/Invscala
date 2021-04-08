class Chords:
    __chords = []

    def set_chords(self, chords_):
        self.__chords = tuple(chords_)

    def get_chords(self):
        return self.__chords


chords = Chords()
