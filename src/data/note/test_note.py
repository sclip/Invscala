import unittest
import note
import music21


note_dummy = note.Notes()
int_dummy = note.NoteInterface()


class TestNote(unittest.TestCase):
    def test_note_name_generation(self):
        n = note_dummy

        # Test maximum values
        self.assertEqual(n.generate_note_names("C4")[-1], "C4")  # Check the last object, should be the same as max
        self.assertEqual(n.generate_note_names("E9")[-1], "E9")
        self.assertEqual(n.generate_note_names("G0")[-1], "G0")

        # Test minimum value default
        self.assertEqual(n.generate_note_names("G0")[0], "A0")
        self.assertEqual(n.generate_note_names("G9")[0], "A0")
        self.assertEqual(n.generate_note_names("E6")[0], "A0")

        # Test minimum value
        self.assertEqual(n.generate_note_names("C4", lowest_note="C3")[-1], "C4")
        self.assertEqual(n.generate_note_names("C4", lowest_note="C3")[0], "C3")
        self.assertEqual(n.generate_note_names("C4", lowest_note="A0")[0], "A0")
        self.assertEqual(n.generate_note_names("A4", lowest_note="A0")[0], "A0")
        self.assertEqual(n.generate_note_names("G9", lowest_note="A0")[0], "A0")
        self.assertEqual(n.generate_note_names("G0", lowest_note="A0")[0], "A0")

        # Various tests
        self.assertEqual(n.generate_note_names("E6")[1], "A#0")
        self.assertEqual(n.generate_note_names("G2")[2], "B0")
        self.assertEqual(n.generate_note_names("G2")[12], "A1")
        self.assertEqual(n.generate_note_names("E2")[24], "A2")

        self.assertEqual(n.generate_note_names("A0")[-1], "A0")
        self.assertEqual(n.generate_note_names("A0")[0], "A0")

        self.assertEqual(n.generate_note_names("A6", lowest_note="A6")[0], "A6")

    def test_note_generation(self):
        n = note_dummy

        notes_names1 = n.generate_note_names("C3")

        self.assertEqual(str(n.generate_notes(notes_names1)[0]), "<music21.note.Note A>")
        self.assertEqual(str(n.generate_notes(notes_names1)[1]), "<music21.note.Note A#>")
        self.assertEqual(str(n.generate_notes(notes_names1)[2]), "<music21.note.Note B>")
        self.assertEqual(str(n.generate_notes(notes_names1)[-1]), "<music21.note.Note C>")

    def test_set_get_notes(self):
        n = note_dummy
        notes_names = n.generate_note_names("C3")
        notes = n.generate_notes(notes_names)

        self.assertEqual(len(n.get_notes()), 0)

        n.set_notes(notes)

        self.assertEqual(str(n.get_notes()[0]), "<music21.note.Note A>")
        self.assertEqual(str(n.get_notes()[-1]), "<music21.note.Note C>")

    def test_transpose(self):
        note_a = music21.note.Note("A0")
        note_c = music21.note.Note("C0")
        self.assertEqual(note_dummy.transpose(note_a, "m3").name, note_c.name)
        self.assertEqual(note_dummy.transpose(note_a, 3).name, note_c.name)


class TestNoteInterface(unittest.TestCase):
    def test_generate(self):
        self.assertEqual(str(int_dummy.generate()[0]), "<music21.note.Note A>")
        self.assertEqual(str(int_dummy.generate()[-1]), "<music21.note.Note G>")

        self.assertEqual(str(int_dummy.generate(lowest="C3")[0]), "<music21.note.Note C>")
        self.assertEqual(str(int_dummy.generate(highest="C3")[-1]), "<music21.note.Note C>")
        self.assertEqual(str(int_dummy.generate(lowest="B2", highest="C3")[-1]), "<music21.note.Note C>")
        self.assertEqual(str(int_dummy.generate(lowest="B2", highest="C3")[0]), "<music21.note.Note B>")


if __name__ == '__main__':
    unittest.main()
