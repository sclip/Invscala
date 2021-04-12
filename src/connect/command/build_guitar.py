from src.connect.command import command
from src.connect.html_builder import build_helper


class BuildGuitar(command.Command):
	def __init__(self, highest_fret, string_count, strings, min_strings, max_strings):
		self.highest_fret = highest_fret

		self.string_count = string_count
		self.strings = strings

		self.min_strings = min_strings
		self.max_strings = max_strings

	def execute(self) -> None:
		build_helper.build_fret_numbering(self.highest_fret)
		build_helper.build_string(self.string_count)
		for string in self.strings:
			build_helper.build_frets(self.highest_fret, string, self.strings.index(string))
		build_helper.build_string_selection(self.min_strings, self.max_strings, self.string_count)
