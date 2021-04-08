import unittest
import guitar
from src.data.defaults import syn_notes

# while
my_guitar = guitar.Guitar(testing=True)
# gently weeps

syn_notes_ = {
	"A#": "Bb",
	"C#": "Db",
	"D#": "Eb",
	"F#": "Gb",
	"G#": "Ab"
}
syn_notes.syn_notes.set_syn_notes(syn_notes_)


class TestGuitar(unittest.TestCase):
	def test_aaa_generate_strings(self):  # added aaa to make this run first
		# DO NOT DELETE "AAA"
		my_guitar.generate_strings()
		self.assertEqual(len(my_guitar.strings), 6)
		self.assertEqual(my_guitar.strings[0].get_name(), "e")
		self.assertEqual(my_guitar.get_string_by_id(0).get_name(), "e")
		self.assertEqual(my_guitar.get_string_by_id(1).get_name(), "B")
		self.assertEqual(my_guitar.get_string_by_id(2).get_name(), "G")
		self.assertEqual(my_guitar.get_string_by_id(3).get_name(), "D")
		self.assertEqual(my_guitar.get_string_by_id(4).get_name(), "A")
		self.assertEqual(my_guitar.get_string_by_id(5).get_name(), "E")

	def test_get_lowest_chord(self):  # TODO: INCOMPLETE!
		# my_guitar.generate_strings()
		# self.assertEqual(my_guitar.get_lowest_chord(music21.chord.Chord("C E G")), ['x', 3, 2, 0, 1, 0])  # C
		# self.assertEqual(my_guitar.get_lowest_chord(music21.chord.Chord("E G# B")), [0, 2, 2, 1, 0, 0])  # E
		# self.assertEqual(my_guitar.get_lowest_chord(music21.chord.Chord("E G B")), [0, 2, 2, 0, 0, 0])  # Em
		pass

	def test_caged(self):
		pass
		"""
		chords = {
			"major": {
				"C": ["x", 3, 2, 0, 1, 0],
				"A": ["x", 0, 2, 2, 2, 0],
				"G": [3, 2, 0, 0, 0, 3],
				"E": [0, 2, 2, 1, 0, 0],
				"D": ["x", "x", 0, 2, 3, 2]
			},
			"minor": {
				"A": ["x", 0, 2, 2, 1, 0],
				"E": [0, 2, 2, 0, 0, 0],
				"D": ["x", "x", 0, 2, 3, 1]
			}
		}
		c = music21.chord.Chord
		func = my_guitar.get_lowest_caged_chord
		# A Shapes
		self.assertEqual(func(c("C E G"), caged_chords=chords), ['x', 3, 5, 5, 5, 3])
		self.assertEqual(func(c("B D# F#"), caged_chords=chords), ['x', 2, 4, 4, 4, 2])
		self.assertEqual(func(c("A C E"), caged_chords=chords), ['x', 0, 2, 2, 1, 0])
		self.assertEqual(func(c("C Eb G"), caged_chords=chords), ['x', 3, 5, 5, 4, 3])

		# E Shapes
		self.assertEqual(func(c("E G B"), caged_chords=chords), [0, 2, 2, 0, 0, 0])
		self.assertEqual(func(c("F A C"), caged_chords=chords), [1, 3, 3, 2, 1, 1])
		self.assertEqual(func(c("Gb Bb Db"), caged_chords=chords), [2, 4, 4, 3, 2, 2])
		self.assertEqual(func(c("Gb A Db"), caged_chords=chords), [2, 4, 4, 2, 2, 2])
		self.assertEqual(func(c("E G# B"), caged_chords=chords), [0, 2, 2, 1, 0, 0])

		# D Shapes
		self.assertEqual(func(c("D F# A"), caged_chords=chords), ["x", "x", 0, 2, 3, 2])
		self.assertEqual(func(c("D F A"), caged_chords=chords), ["x", "x", 0, 2, 3, 1])
		self.assertEqual(func(c("Eb Gb Bb"), caged_chords=chords), ["x", "x", 1, 3, 4, 2])
		"""


if __name__ == '__main__':
	unittest.main()
