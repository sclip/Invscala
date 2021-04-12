from src.data.searcher import searcher, chord_searcher
import unittest
import music21


c = music21.chord.Chord
chord_sample = [c("C E G"), c("D F# G"), c("C D G")]


class TestSearcher(unittest.TestCase):
	def test_searcher(self):

		def searching_method(self_, index, to_index, results_len) -> list:
			to_return = []

			for item in to_index:
				if item.startswith(index):
					to_return.append(item)

			return to_return

		test_searcher = searcher.Searcher(searching_method)
		search_results1 = test_searcher.search("ab", ["a", "b", "c", "ab", "abc", "abcd"])
		search_results2 = test_searcher.search("a", ["a", "b", "c", "ab", "abc", "abcd"])
		search_results3 = test_searcher.search("b", ["a", "b", "c", "ab", "abc", "abcd", "bc"])

		self.assertTrue("ab" in search_results1)
		self.assertTrue("ab" in search_results2)
		self.assertFalse("b" in search_results1)
		self.assertFalse("b" in search_results2)
		self.assertFalse("a" in search_results3)
		self.assertFalse("c" in search_results3)
		self.assertTrue("bc" in search_results3)
		self.assertEqual(search_results1, ('ab', 'abc', 'abcd'))

	def test_chord_searching_methods(self):
		res1 = chord_searcher._find_from_first_letters(
			chord_searcher.chord_searcher,
			"c",
			chord_sample,
			0
		)
		self.assertEqual(chord_searcher.chord_searcher.action(c("C E G")), "C Major")
		self.assertEqual(res1[0], "C Major")

	def test_chord_searcher(self):
		res1 = chord_searcher.chord_searcher.search("c", chord_sample)
		self.assertEqual(res1[0], "C Major")


if __name__ == '__main__':
	unittest.main()
