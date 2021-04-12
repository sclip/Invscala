from src.data.searcher import searcher, chord_searcher


class IndexerFacade:
	def __init__(self):
		self._indexer = indexer.Indexer
