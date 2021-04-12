class Searcher:

	"""
	Class for searching to collections of objects

	Subclass it to change default behavior, provide it with search methods to use it.
	More than one searching method may be used.
	Search methods are given the following arguments by default: self, index, to_search, len(to_return);
		self: 			The searching class
		index:			Search keyword
		to_search:		Collection of items to search through
		len(to_return):	Current amount of found results

	Override `run_search_methods` to change the above behavior.

	Override `prepare` to change things before any logic is run

	Override `finalize` to change what is done right before the results are returned.

	All the above methods must have a `return` statement!

	Example:
		def searching_method(self, index, to_index, results_len) -> list:
			to_return = []

			for item in to_index:
				if item.startswith(index):
					to_return.append(item)

			return to_return

		my_searcher = Searcher(searching_method)
		my_searcher.search()

	"""

	def __init__(self, *search_methods):
		self._search_methods = search_methods
		self.__index = None
		self.__to_search = []
		self.__to_return = []

	def search(self, index, to_search) -> tuple:
		"""

		Searches through a collection of items, and returns matching items

		Args:
			index: Search keyword
			to_search: Items to search through, must be iterable

		Returns:
			Matching items

		"""

		self.__to_return = []
		self.__to_search = tuple(to_search)
		self.__index = index

		self.prepare()

		# If index is empty then we return everything in to_search
		self.on_empty_search()

		# Other logic
		self.run_search_methods(
			self.__index,
			self.__to_search,
			self.__to_return
		)

		self.finalize()

		return tuple(self.__to_return)

	def run_search_methods(self, index, to_search, to_return):
		# Runs every searching method
		for search_method in self._search_methods:
			[to_return.append(result) for result in search_method(self, index, to_search, len(to_return))]
		return to_return

	def on_empty_search(self):
		if len(self.__index) == 0:
			try:
				self.__to_return = [self.action(x) for x in self.__to_search]
			except TypeError:
				raise TypeError(f"'{type(self.__to_search)}' object is not iterable, and cannot be searched through.")

	def action(self, item):
		return item

	def prepare(self):
		pass

	def finalize(self):
		pass
