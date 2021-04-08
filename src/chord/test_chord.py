import unittest
import chord
import music21
from src.defaults import chords
from src.defaults import syn_notes


chord_builder_dummy = chord.ChordBuilder
cbd = chord_builder_dummy

syn_notes_ = {
  "A#": "Bb",
  "C#": "Db",
  "D#": "Eb",
  "F#": "Gb",
  "G#": "Ab"
}
syn_notes.syn_notes.set_syn_notes(syn_notes_)


class ChordBuilderTestCase(unittest.TestCase):
    def test_major_chord(self):
        c_maj = music21.chord.Chord(["C", "E", "G"])
        c_maj2 = cbd.generate_major()
        self.assertEqual(str(c_maj), str(c_maj2))

        d_maj = music21.chord.Chord(["D", "F#", "A"])
        d_maj2 = cbd.generate_major().transpose(2)
        self.assertEqual(str(d_maj), str(d_maj2))

    def test_minor_chord(self):
        c_min = music21.chord.Chord(["C", "Eb", "G"])
        c_min2 = cbd.generate_minor()
        self.assertEqual(str(c_min), str(c_min2))

        c_min = music21.chord.Chord(["D", "F", "A"])
        c_min2 = cbd.generate_minor().transpose(2)
        self.assertEqual(str(c_min), str(c_min2))

    def test_dim_chord(self):
        c = music21.chord.Chord(["C", "Eb", "Gb"])
        c2 = cbd.generate_diminished()
        self.assertEqual(str(c), str(c2))

        d = music21.chord.Chord(["D", "F", "G#"])  # Ab doesnt work?
        d2 = cbd.generate_diminished().transpose(2)
        self.assertEqual(str(d), str(d2))

    def test_find_chords(self):
        # set up chords
        c = music21.chord.Chord
        my_chords = [chord.ChordBuilder.generate_major(), chord.ChordBuilder.generate_minor(), c("C E G Bb")]
        chords.chords.set_chords(my_chords)
        my_notes = [music21.note.Note("C"), music21.note.Note("E"), music21.note.Note("G")]
        self.assertEqual(my_chords[0], chord.ChordInterface.find_chord(my_notes)[0])
        self.assertNotEqual(my_chords[2], chord.ChordInterface.find_chord(my_notes)[0])  # C7 is not the same as C
        self.assertEqual(my_chords[2], chord.ChordInterface.find_chord(my_notes)[1])  # Larger chords are returned!
        #                                                                             # (as they should be)
        my_notes = [music21.note.Note("C"), music21.note.Note("Eb"), music21.note.Note("G")]
        self.assertEqual(my_chords[1], chord.ChordInterface.find_chord(my_notes)[0])

        my_notes = [music21.note.Note("C"), music21.note.Note("E"), music21.note.Note("G"), music21.note.Note("Bb")]
        self.assertEqual(my_chords[2], chord.ChordInterface.find_chord(my_notes)[0])

        my_notes = [music21.note.Note("C"), music21.note.Note("D#"), music21.note.Note("G")]  # Fixed!
        self.assertEqual(my_chords[1], chord.ChordInterface.find_chord(my_notes)[0])

    def test_contains_note(self):
        c = music21.chord.Chord
        my_chords = [chord.ChordBuilder.generate_major(), chord.ChordBuilder.generate_minor(), c("C E G Bb")]
        n = music21.note.Note
        for co in my_chords:
            self.assertTrue(chord.ChordInterface.contains_note(co, co.root()))
        self.assertTrue(chord.ChordInterface.contains_note(my_chords[1], n("D#")))
        self.assertFalse(chord.ChordInterface.contains_note(my_chords[0], n("B")))


if __name__ == '__main__':
    unittest.main()
