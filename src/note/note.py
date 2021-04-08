import music21
from string import ascii_uppercase


class Notes:

    __notes = music21.stream.Stream()  # basically a list

    # todo: figure out midi

    def set_notes(self, notes):
        for note in notes:
            self.__notes.append(note)

    def get_notes(self):
        return self.__notes

    @staticmethod
    def transpose(note, interval):
        """

        :param note: Note to transpose. Must be a music21 object
        :param interval: Can be either a string, like "m2", or an int, like "1"
        :return:
        """
        return note.transpose(interval)

    @staticmethod
    def generate_notes(notes_to_generate):
        """generate_notes(notes_to_generate) -> list

        :param notes_to_generate: List of note names, must be 2-length strings with the format <char><int>, eg "C3"
        :return: List with music21 note objects
        """
        notes = []
        for note in notes_to_generate:
            notes.append(music21.note.Note(note))
        return notes

    @staticmethod
    def generate_note_names(highest_note, lowest_note="A0", default_accidental="#"):
        """generate_note_names(highest_note) -> list

        :param lowest_note: Lowest note to generate from. Warning: Should not be higher than highest_note!
        :param highest_note: Highest note to generate up to, ex "C6". Warning: max 1 int!
        :param default_accidental: "#" or "b"
        :rtype: list
        """

        if len(highest_note) == 4:
            print("Error: Value too large")
            return
        if default_accidental != "b" and default_accidental != "#":
            print("Error: Invalid accidental")
            return

        to_return = []

        # Highest note will be something like "C6"
        # The int(highest_note[1]) part grabs the 6
        # the +1 makes it a 7, a break in the loop makes sure that the highest note will be C6 and it'll break
        # after that point
        for number in range(int(lowest_note[-1]), int(highest_note[-1]) + 1):
            # Go through uppercase letters starting at lowest_note[0].
            for letter in ascii_uppercase[ascii_uppercase.index(lowest_note[0]):]:
                if default_accidental == "b" and letter != "C" and letter != "F":  # If we want flat notes
                    to_return.append(letter + "b" + str(number))
                    to_return.append(letter + str(number))
                elif letter != "B" and letter != "E" and (number != int(highest_note[-1]) or letter != highest_note[0]):
                    to_return.append(letter + str(number))
                    to_return.append(letter + "#" + str(number))
                else:
                    to_return.append(letter + str(number))
                if letter == "G":  # We don't want to continue into H and onwards
                    break
                if number == int(highest_note[-1]) and letter == highest_note[0]:  # Prevents a max"C6" from doing "C#6"
                    break

        return to_return


class NoteInterface:
    @staticmethod
    def generate(lowest="A0", highest="G9"):
        note_names = Notes.generate_note_names(highest, lowest_note=lowest)
        notes = Notes.generate_notes(note_names)
        return notes

    @staticmethod
    def generate_octave():
        note_names = Notes.generate_note_names("G#0")  # Generate only one octave worth of notes
        for note in note_names:
            note2 = ""
            for letter in note2:
                if letter == note[-1]:
                    break
                note2 += letter
            note = note2
        notes = Notes.generate_notes(note_names)
        return notes
