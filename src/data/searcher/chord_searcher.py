from src.data.searcher import searcher
from src.data.chord.chord import ChordInterface
from src.data.defaults.syn_notes import syn_notes
from src.data.defaults import chord_types
from difflib import SequenceMatcher


class ChordSearcher(searcher.Searcher):
	def __init__(self, *search_methods):
		super().__init__(*search_methods)

	def action(self, item):
		return ChordInterface.get_chord_name(item)

	def finalize(self, items):
		no_dupes_to_return = items
		# [no_dupes_to_return.append(x) for x in items if x not in no_dupes_to_return]
		return tuple(no_dupes_to_return)  # Todo: implement sorting


#####################
# Searching Methods #
#####################

def _find_from_first_letters(self, index, to_search, results_len) -> list:
	to_return = []

	if len(index) in [1, 2]:
		for chord in to_search:
			if str.casefold(self.action(chord)).startswith(index) is True:
				to_return.append(self.action(chord))
			try:
				# Use of .capitalize instead of .upper stops bb from becoming BB instead of Bb
				new_ind = syn_notes.get_syn_notes()[str.capitalize(index).replace("b", "-")]

				new_ind = str.casefold(new_ind.replace("-", "b"))

				if str.casefold(self.action(chord)).startswith(new_ind) is True:
					to_return.append(self.action(chord))
			except KeyError:
				pass
	return to_return


def _find_in_long(self, index, to_search, results_len) -> list:
	to_return = []

	if len(index) >= 5:
		for chord_type in chord_types.chord_types.get_chord_types():  # Get stuff such as C major, from major
			if index == str.lower(chord_type):
				for chord in to_search:
					if str.casefold(self.action(chord)).__contains__(index):
						to_return.append(self.action(chord))
			elif (len(chord_type) >= 8 and SequenceMatcher(None, str.lower(chord_type), index).ratio() > 0.85) or \
				(len(chord_type) < 8 and SequenceMatcher(None, str.lower(chord_type), index).ratio() >= 0.79):
				# 0.8 is the magic number for any likely misspelling of major or minor being similar enough
				for chord in to_search:
					if str.casefold(self.action(chord)).__contains__(str.lower(chord_type)):
						to_return.append(self.action(chord))
	return to_return


def _find_minor(self, index, to_search, results_len) -> list:
	to_return = []

	if results_len == 0:
		try:
			if index[1] == "m":  # If we have Em for example
				for chord in to_search:
					if chord.quality == "minor" and str.casefold(chord.root().name) == index[0]:
						to_return.append(self.action(chord))
			elif index[2] == "m":
				for chord in to_search:
					if chord.quality == "minor" and str.lower(self.action(chord)).startswith(
							index[0] + index[1]) is True:
						to_return.append(self.action(chord))
		except IndexError:
			return []
	return to_return


def _final(self, index, to_search, results_len) -> list:
	to_return = []

	if results_len == 0:  # only if we don't have any valid chords already
		for chord in to_search:
			if str.lower(self.action(chord)).startswith(index) is True:
				to_return.append(self.action(chord))

		if len(to_return) == 0:  # similarity search
			for chord in to_search:
				if SequenceMatcher(None, str.casefold(self.action(chord)), index).ratio() > 0.8:
					to_return.append(self.action(chord))

			if len(to_return) == 0:  # if it's still 0, lower accuracy
				for chord in to_search:
					if SequenceMatcher(None, str.casefold(self.action(chord)), index).ratio() > 0.75:
						to_return.append(self.action(chord))

	return to_return


# The order of things matters!
chord_searcher = ChordSearcher(
	_find_from_first_letters,
	_find_in_long,
	_find_minor,
	_final
)
