from src.data.instrument import instrument
from src.data.instrument.guitar import guitar_string
from src.connect.command import build_guitar
from src.data.defaults import default


class Guitar(instrument.Instrument):
	def __init__(self, settings=None):
		if settings is None:
			if not default.settings.loaded_settings:
				return
			settings = default.settings.get_settings_file("guitar")
		elif type(settings) is str:
			settings = default.settings.get_settings_file(settings)

		self._lowest_fret = 0
		self._highest_fret = settings["Default Highest Fret"]
		self._maximum_fret = settings["Default Maximum Fret"]

		self._string_count = settings["Default String Count"]
		self._min_strings = settings["Minimum String Count"]
		self._max_strings = settings["Maximum String Count"]
		self._string_names = settings["String Names"]
		self._string_notes = settings["String Notes"]

		self._strings = self._generate_strings()

	def _generate_strings(self) -> list:
		strings = []
		for i in range(self._string_count):
			strings.append(guitar_string.generate_string(
				self._string_names[i],
				self._lowest_fret,
				self._highest_fret,
				starting_note=self._string_notes[i],
				num=i
			))
		return strings

	@property
	def strings(self) -> list:  # strings[0] is always the highest string!
		return self._strings

	@property
	def string_count(self) -> int:
		return self._string_count

	def string(self, n) -> guitar_string.GuitarString:
		return self._strings[n]

	def init(self):
		settings = default.settings.get_settings_file("guitar")

		self._lowest_fret = 0
		self._highest_fret = settings["Default Highest Fret"]
		self._maximum_fret = settings["Default Maximum Fret"]

		self._string_count = settings["Default String Count"]
		self._min_strings = settings["Minimum String Count"]
		self._max_strings = settings["Maximum String Count"]
		self._string_names = settings["String Names"]
		self._string_notes = settings["String Notes"]

		self._strings = self._generate_strings()

	def build(self) -> None:
		build = build_guitar.BuildGuitar(
			self._highest_fret,
			self._string_count,
			self._strings,
			self._max_strings,
			self._min_strings
		)
		build.execute()


guitar = Guitar()
