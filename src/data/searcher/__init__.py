from src.data.searcher import searcher, chord_searcher


class SearchFacade:
	def __init__(self):
		self._chord_searcher = chord_searcher.chord_searcher
		self._scale_searcher = None
		self._interval_searcher = None

	def search_chords(self, index):
		self._chord_searcher.search(index)


search = SearchFacade()
