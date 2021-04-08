import unittest
import syn_notes
import music21


syn_notes_ = {
  "A#": "Bb",
  "C#": "Db",
  "D#": "Eb",
  "F#": "Gb",
  "G#": "Ab"
}
syn_notes.syn_notes.set_syn_notes(syn_notes_)


class SynNotesTestCase(unittest.TestCase):
    def test_is_syn_note(self):
        self.assertNotEqual("A#", "Bb")
        n = music21.note.Note
        self.assertTrue(syn_notes.syn_notes.is_syn_note(n("A#"), n("Bb")))
        self.assertTrue(syn_notes.syn_notes.is_syn_note(n("C#"), n("Db")))
        self.assertTrue(syn_notes.syn_notes.is_syn_note(n("D#"), n("Eb")))
        self.assertTrue(syn_notes.syn_notes.is_syn_note(n("F#"), n("Gb")))
        self.assertTrue(syn_notes.syn_notes.is_syn_note(n("G#"), n("Ab")))
        self.assertTrue(syn_notes.syn_notes.is_syn_note(n("Ab"), n("G#")))
        self.assertTrue(syn_notes.syn_notes.is_syn_note(n("E-"), n("D#")))
        self.assertFalse(syn_notes.syn_notes.is_syn_note(n("A"), n("B")))
        self.assertFalse(syn_notes.syn_notes.is_syn_note(n("A"), n("Bb")))
        self.assertFalse(syn_notes.syn_notes.is_syn_note(n("A"), n("B-")))
        self.assertFalse(syn_notes.syn_notes.is_syn_note(n("Bb"), n("B")))


if __name__ == '__main__':
    unittest.main()
