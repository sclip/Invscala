import unittest
import music21
from src.data.chord import guitar_chord_builder
from common.guitar import guitar


my_guitar = guitar.Guitar(testing=True)
my_guitar.generate_strings()


c = music21.chord.Chord
c_chord = c("C E G")
mb1 = guitar_chord_builder.GuitarChord(c_chord, 4, string_holder=my_guitar)


class TestCase(unittest.TestCase):
	def test_get_chord_frets(self):
		mc = music21.chord.Chord("C E G")
		gcb = guitar_chord_builder._get_chord_frets(mc, my_guitar)
		self.assertEqual(gcb[1][0].get_note_name(), "C")
		for x in gcb:
			for y in x:
				self.assertEqual(y.get_note_name() in ["C", "E", "G"], True)

		mc = music21.chord.Chord("A C E")
		gcb = guitar_chord_builder._get_chord_frets(mc, my_guitar)
		for x in gcb:
			for y in x:
				self.assertEqual(y.get_note_name() in ["A", "C", "E"], True)

		mc = music21.chord.Chord("D F# G")
		gcb = guitar_chord_builder._get_chord_frets(mc, my_guitar)
		for x in gcb:
			for y in x:
				self.assertEqual(y.get_note_name() in ["D", "F#", "G"], True)

		mc = music21.chord.Chord("C E G B")
		gcb = guitar_chord_builder._get_chord_frets(mc, my_guitar)
		for x in gcb:
			for y in x:
				self.assertEqual(y.get_note_name() in ["C", "E", "G", "B"], True)

		mc = music21.chord.Chord("A B C")
		gcb = guitar_chord_builder._get_chord_frets(mc, my_guitar)
		for x in gcb:
			for y in x:
				self.assertEqual(y.get_note_name() in ["A", "B", "C"], True)

		mc = music21.chord.Chord("G C D")
		gcb = guitar_chord_builder._get_chord_frets(mc, my_guitar)
		for x in gcb:
			for y in x:
				self.assertEqual(y.get_note_name() in ["G", "C", "D"], True)

		mc = music21.chord.Chord("E F")
		gcb = guitar_chord_builder._get_chord_frets(mc, my_guitar)
		for x in gcb:
			for y in x:
				self.assertEqual(y.get_note_name() in ["E", "F"], True)

	def test_get_frets_on_string(self):
		mc = music21.chord.Chord("C E G")
		mb = guitar_chord_builder.GuitarChord(mc, 1)
		prev = 3
		string = guitar_chord_builder._get_chord_frets(mc, my_guitar)[3]
		func = mb._get_frets_on_string(prev, string, guit=my_guitar)
		self.assertEqual(func[0].get_note_name(), "E")
		self.assertEqual(func[0].get_number(), 2)
		prev = 2
		string = guitar_chord_builder._get_chord_frets(mc, my_guitar)[2]
		func = mb._get_frets_on_string(prev, string, guit=my_guitar)
		self.assertEqual(func[0].get_note_name(), "G")
		self.assertEqual(func[0].get_number(), 0)

		prev = 15
		string = guitar_chord_builder._get_chord_frets(mc, my_guitar)[3]
		func = mb._get_frets_on_string(prev, string, guit=my_guitar, bass_fret=15)
		self.assertEqual(func[0].get_number(), 14)

	def test_check_validity(self):
		pass

	def test_find_chord_shapes(self):
		mb = guitar_chord_builder.GuitarChord(c("C E G"), 4, string_holder=my_guitar)
		mb.get_shapes()
		print(mb.get_shapes())


if __name__ == '__main__':
	unittest.main()
