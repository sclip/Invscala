from src.connect.command import command
from src.data.defaults import chords
from src.data import searcher
import eel


class Search(command.Command):
	""" Comment """

	def __init__(self, type_):
		self._index = ""
		self._type = type_
		self._results = tuple([])

	@property
	def index(self):
		return self._index

	@index.setter
	def index(self, value):
		self._index = value

	@property
	def result(self):
		return self._results

	def execute(self) -> None:
		# Todo: Use switch with py 3.10
		try:
			raise SyntaxError  # Todo: Replace with match
		except SyntaxError:
			if self._type == "Chords":
				self._results = searcher.search(self._index, tuple(chords.chords.get_chords()))
			else:
				raise TypeError(f"{self._type} is not a valid type")

		for obj in self._results:
			eel.search_append(obj, self._type)


@eel.expose
def search(index, type_):
	search_ = Search(type_)
	search_.index = index
	search_.execute()
