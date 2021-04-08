import unittest
import guitar_string
import music21


class TestGuitarString(unittest.TestCase):

	def test_generate_string_and_get_fret(self):
		my_new_string = guitar_string.generate_string("B", 0, 24, "B3")
		self.assertEqual(my_new_string.get_name(), "B")
		self.assertEqual(len(my_new_string.get_frets()), 24)
		self.assertEqual(my_new_string.get_fret(0).get_name(), "B0")
		self.assertEqual(my_new_string.get_fret(0).get_note(), music21.note.Note("B3"))
		self.assertEqual(my_new_string.get_fret(23).get_note(), music21.note.Note("B-5"))
		self.assertEqual(my_new_string.get_fret(12).get_note(), music21.note.Note("B4"))
		self.assertEqual(str(my_new_string.get_fret(1).get_note()), str(music21.note.Note("C3")))

	def test_select_fret(self):
		my_new_string = guitar_string.generate_string("E", 0, 24, "E4")
		self.assertIsNone(my_new_string.get_selected_fret())

		my_new_string.select_fret(4)
		self.assertIsNotNone(my_new_string.get_selected_fret())
		self.assertEqual(my_new_string.get_selected_fret(), my_new_string.get_fret(4))
		my_new_string.select_fret(4)
		self.assertIsNone(my_new_string.get_selected_fret())
		my_new_string.select_fret(4)
		self.assertIsNotNone(my_new_string.get_selected_fret())
		my_new_string.select_fret(6)
		self.assertIsNotNone(my_new_string.get_selected_fret())
		my_new_string.select_fret(6)
		self.assertIsNone(my_new_string.get_selected_fret())

	def test_highlight_fret(self):
		my_new_string = guitar_string.generate_string("E", 0, 24, "E4")
		self.assertEqual(my_new_string.get_highlighted_frets(), [])
		my_new_string.highlight_fret(5)
		self.assertEqual(my_new_string.get_highlighted_frets()[0], my_new_string.get_fret(5))

		my_new_string.highlight_fret(5)
		self.assertEqual(my_new_string.get_highlighted_frets(), [])

	def test_transpose_string(self):
		my_new_string = guitar_string.generate_string("E", 0, 24, "E4")
		n = music21.note.Note
		self.assertEqual(my_new_string.get_name(), "e")
		self.assertEqual(my_new_string.get_fret(0).get_name(), "E0")
		self.assertEqual(str(my_new_string.get_fret(0).get_note()), str(n("e")))
		self.assertEqual(my_new_string.get_fret(5).get_name(), "E5")
		self.assertEqual(str(my_new_string.get_fret(5).get_note()), str(n("A")))

		my_new_string.change_tuning(1)  # Change to F
		self.assertEqual(my_new_string.get_name(), "E")
		self.assertEqual(my_new_string.get_fret(0).get_name(), "E0")
		self.assertEqual(str(my_new_string.get_fret(0).get_note()), str(n("F")))
		self.assertEqual(my_new_string.get_fret(5).get_name(), "E5")
		self.assertEqual(str(my_new_string.get_fret(5).get_note()), str(n("B-")))

		my_new_string.change_tuning(-1)  # Change back to E
		self.assertEqual(my_new_string.get_name(), "E")
		self.assertEqual(my_new_string.get_fret(0).get_name(), "E0")
		self.assertEqual(str(my_new_string.get_fret(0).get_note()), str(n("E")))
		self.assertEqual(my_new_string.get_fret(5).get_name(), "E5")
		self.assertEqual(str(my_new_string.get_fret(5).get_note()), str(n("A")))

		my_new_string.change_tuning(-2)  # Change to D
		self.assertEqual(my_new_string.get_name(), "E")
		self.assertEqual(my_new_string.get_fret(0).get_name(), "E0")
		self.assertEqual(str(my_new_string.get_fret(0).get_note()), str(n("D")))
		self.assertEqual(my_new_string.get_fret(5).get_name(), "E5")
		self.assertEqual(str(my_new_string.get_fret(5).get_note()), str(n("G")))

		my_new_string.reset_tuning()  # Change back to E
		self.assertEqual(my_new_string.get_name(), "E")
		self.assertEqual(my_new_string.get_fret(0).get_name(), "E0")
		self.assertEqual(str(my_new_string.get_fret(0).get_note()), str(n("E")))
		self.assertEqual(my_new_string.get_fret(5).get_name(), "E5")
		self.assertEqual(str(my_new_string.get_fret(5).get_note()), str(n("A")))

		my_new_string.change_tuning(5)  # Change to A
		self.assertEqual(my_new_string.get_name(), "E")
		self.assertEqual(my_new_string.get_fret(0).get_name(), "E0")
		self.assertEqual(str(my_new_string.get_fret(0).get_note()), str(n("A")))
		self.assertEqual(my_new_string.get_fret(5).get_name(), "E5")
		self.assertEqual(str(my_new_string.get_fret(5).get_note()), str(n("D")))

		my_new_string.reset_tuning()  # Change back to E
		self.assertEqual(my_new_string.get_name(), "E")
		self.assertEqual(my_new_string.get_fret(0).get_name(), "E0")
		self.assertEqual(str(my_new_string.get_fret(0).get_note()), str(n("E")))
		self.assertEqual(my_new_string.get_fret(5).get_name(), "E5")
		self.assertEqual(str(my_new_string.get_fret(5).get_note()), str(n("A")))


if __name__ == '__main__':
	unittest.main()
