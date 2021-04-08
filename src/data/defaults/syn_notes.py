import music21


class SynNotes:
    __syn_notes = {}  # "Synonymous" notes, ex Bb and A#

    def set_syn_notes(self, notes_):  # Input [["A#", "Bb"], [], []]
        n = music21.note.Note  # Doing this makes it so that Bb becomes B-
        for note in notes_:
            self.__syn_notes.setdefault(n(note).name, n(notes_[note]).name)
            self.__syn_notes.setdefault(n(notes_[note]).name, n(note).name)  # Reversed

    def get_syn_notes(self):
        return self.__syn_notes

    def get_reversed_syn_notes(self):
        return dict(map(reversed, self.__syn_notes.items()))

    def is_syn_note(self, note_a, note_b):
        try:
            if note_a.name == note_b.name:
                return True
            elif note_a.name == self.__syn_notes[note_b.name] or note_b.name == self.__syn_notes[note_a.name]:
                return True
        except KeyError:
            return False
        return False


syn_notes = SynNotes()
