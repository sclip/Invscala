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

	Override `prepare` to change things to `to_search`

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

	def search(self, index, to_search) -> tuple:
		"""

		Searches through a collection of items, and returns matching items

		Args:
			index: Search keyword
			to_search: Items to search through, must be iterable

		Returns:
			Matching items

		"""

		to_return = []
		to_search = tuple(to_search)

		to_search = self.prepare(to_search)

		# If index is empty then we return everything in to_search
		if len(index) == 0:
			try:
				to_return = [self.action(x) for x in to_search]
			except TypeError:
				raise TypeError(f"'{type(to_search)}' object is not iterable, and cannot be searched through.")

		# Other logic
		self.run_search_methods(
			index,
			to_search,
			to_return
		)

		to_return = self.finalize(to_return)

		return to_return

	def run_search_methods(self, index, to_search, to_return):
		# Runs every searching method
		for search_method in self._search_methods:
			[to_return.append(result) for result in search_method(self, index, to_search, len(to_return))]
		return to_return

	def action(self, item):
		return item

	def prepare(self, items):
		return items

	def finalize(self, items) -> tuple:
		return tuple(sorted(items))
