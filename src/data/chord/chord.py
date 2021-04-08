import music21
from src.data.defaults import syn_notes, chord_types, chords as chords_list
from difflib import SequenceMatcher
from tools import sentence_splitter

_chords = {}  # {major: [...], minor: [...], ...}
all_chords = []


class ChordBuilder:
	@staticmethod
	def generate_major():
		return music21.chord.Chord([0, 4, 7])

	@staticmethod
	def generate_minor():
		return music21.chord.Chord([0, 3, 7])

	@staticmethod
	def generate_diminished():
		return music21.chord.Chord([0, 3, 6])


class ChordInterface:
	@staticmethod
	def init():  # Generate all chords and add them to the _chords dictionary.
		get_chord_types = chord_types.chord_types.get_chord_types
		for chord_type in get_chord_types():
			# _chords.setdefault(chord_type, music21.chord.Chord(get_chord_types()[chord_type]))
			# Only generate C-chords, then use the transpose functions to generate the necessary ones on the fly
			all_chords.append(music21.chord.Chord(get_chord_types()[chord_type]))
		ac = tuple(all_chords.copy())
		for i in range(1, 11):
			for c in ac:
				new_chord = c.transpose(i)
				if new_chord.commonName[0] == "e":  # if it begins with e then it very likely is broken
					new_chord = ChordInterface.fix_chord(new_chord)
				all_chords.append(new_chord)
		ac = tuple(all_chords.copy())
		for c in ac:
			print(
				f"Chord: {ChordInterface.get_chord_name(c)}, content: {[x.name for x in c.notes]}, root: {c.root().name}")
		print("yee")

	@staticmethod
	def fix_chord(chord):
		syn_notes_1 = {"A#": "B-", "C#": "D-", "D#": "E-", "F#": "G-", "G#": "A-"}
		syn_notes_2 = dict(map(reversed, syn_notes_1.items()))  # pycharm complains, but this does work.

		for c_type in ["major triad", "minor triad", "diminished triad"]:
			if chord.commonName == f"enharmonic equivalent to {c_type}":
				new_notes = []
				for note in chord.notes:
					note_name = note.name
					try:
						new_notes.append(syn_notes_1[note_name])
					except KeyError:
						new_notes.append(note_name)
				chord = music21.chord.Chord(new_notes)

			if chord.commonName == f"enharmonic equivalent to {c_type}":
				new_notes = []
				for note in chord.notes:
					note_name = note.name
					try:
						new_notes.append(syn_notes_2[note_name])
					except KeyError:
						new_notes.append(note_name)
				chord = music21.chord.Chord(new_notes)

			if chord.commonName == f"enharmonic equivalent to {c_type}":
				print(f"Error: Broken chord \nChord name: {chord.root()} {chord.commonName} \nContent: {chord.notes}")

		return chord

	@staticmethod
	def get_third(chord):
		return chord.third

	@staticmethod
	def get_fifth(chord):
		return chord.fifth

	@staticmethod
	def get_seventh(chord):
		return chord.seventh

	@staticmethod
	def get_notes(chord):
		return chord.notes

	@staticmethod
	def get_root(chord):
		return chord.root

	@staticmethod
	def transpose_chord(chord, dist):
		"""

		:param chord: Chord to transpose from
		:param dist: Distance to transpose, in semitones or intervals
		:type chord: music21.chord.Chord
		:return:
		"""
		return chord.transpose(dist)

	@staticmethod
	def get_chord_name(chord, strip_root=False):

		new_root = None
		type_ = chord.commonName
		for c_type in ["major triad", "minor triad", "diminished triad"]:
			if chord.commonName == f"enharmonic equivalent to {c_type}":
				new_name = sentence_splitter.split(c_type)[0]
				new_root = chord.bass()
				if new_name != "diminished":
					type_ = new_name
				else:
					type_ = c_type
			if chord.commonName == c_type:
				new_name = sentence_splitter.split(c_type)[0]
				if new_name != "diminished":
					type_ = new_name
				else:
					type_ = c_type
		new_name = ""
		for n in range(len(type_)):  # Make each word uppercase
			if n == 0:
				new_name += str.upper(type_[0])
			elif type_[n - 1] == " ":
				new_name += str.upper(type_[n])
			else:
				new_name += type_[n]

		chord_name = ""
		try:  # avoid annoying bug when calling chord.root()
			if new_root is None:
				root = chord.root().name
			else:
				root = new_root.name
			if strip_root is False:
				if root == "G-":  # Make names more consistent, avoid weird stuff like Gb Major and F# Diminished
					root = "F#"
				elif root == "A-":
					root = "G#"
				elif root == "A#":
					root = "B-"
				elif root == "D-":
					root = "C#"
				elif root == "D#":
					root = "E-"
				chord_name = f"{root.replace('-', 'b')} {new_name}"  # Turn B- into Bb, D- into Db, etc
			else:
				chord_name = f"{new_name}"
		except music21.chord.ChordException:
			print(f"Error: broken chord {chord.commonName}, no pitches")
		return chord_name

	@staticmethod
	def contains_note(chord, note_to_find):
		for note in chord.notes:
			if note.name == note_to_find.name or syn_notes.syn_notes.is_syn_note(note, note_to_find) is True:
				return True
		return False

	@staticmethod
	def find_chord(notes):
		matching_chords = []
		req_matches = len(notes)
		for chord in chords_list.chords.get_chords():
			matches = 0
			for note_ in notes:
				for note in chord.notes:
					if note.name == note_.name or syn_notes.syn_notes.is_syn_note(note, note_):
						# 2nd part checks that D# and Eb are the "same"
						matches += 1
			if matches >= req_matches:
				matching_chords.append(chord)
		return matching_chords

	@staticmethod
	def get_chord(chord_name):
		for chord in chords_list.chords.get_chords():
			if str.casefold(ChordInterface.get_chord_name(chord)) == str.casefold(chord_name):
				return chord
		print(f"No chords found with the name: {chord_name}")
		print(f"Debug Info:\n----------\nInput Name: {chord_name}\nCasefolded: {str.casefold(chord_name)}\nIn chords: "
			  f"{str.casefold(chord_name) in chords_list.chords.get_chords()}")

	# Todo: chord_sort(), alternative to sort()

	@staticmethod
	def index(index):  # todo: potentially move to its own module, add to_search as param
		to_return = []
		to_search = tuple(chords_list.chords.get_chords())

		index = str.casefold(str(index))

		print(f"searching {index}")

		if len(index) == 0:
			for chord in to_search:
				to_return.append(ChordInterface.get_chord_name(chord))
			return sorted(to_return)  # todo: improve sort

		# if only 1 letter is typed in then find all suitable scales, ex C -> C major, c minor, etc
		if len(index) == 1 or len(index) == 2:
			for chord in to_search:
				if str.lower(ChordInterface.get_chord_name(chord)).startswith(index) is True:
					to_return.append(ChordInterface.get_chord_name(chord))
				try:
					# Use of .capitalize instead of .upper stops bb from becoming BB instead of Bb
					new_ind = syn_notes.syn_notes.get_syn_notes()[str.capitalize(index).replace("b", "-")]
					new_ind = str.lower(new_ind.replace("-", "b"))
					if str.lower(ChordInterface.get_chord_name(chord)).startswith(new_ind) is True:
						to_return.append(ChordInterface.get_chord_name(chord))
				except KeyError:
					pass
		elif len(index) >= 5:  # Check for at least 5 letters
			for chord_type in chord_types.chord_types.get_chord_types():  # Get stuff such as C major, from major
				if index == str.lower(chord_type):
					for chord in to_search:
						if str.casefold(ChordInterface.get_chord_name(chord)).__contains__(index):
							to_return.append(ChordInterface.get_chord_name(chord))
				elif (len(chord_type) >= 8 and SequenceMatcher(None, str.lower(chord_type), index).ratio() > 0.85) or \
						(len(chord_type) < 8 and SequenceMatcher(None, str.lower(chord_type), index).ratio() >= 0.79):
					# 0.8 is the magic number for any likely misspelling of major or minor being similar enough
					for chord in to_search:
						if str.casefold(ChordInterface.get_chord_name(chord)).__contains__(str.lower(chord_type)):
							to_return.append(ChordInterface.get_chord_name(chord))

		if len(to_return) == 0:
			if index[1] == "m":  # If we have Em for example
				for chord in to_search:
					if chord.quality == "minor" and str.casefold(chord.root().name) == index[0]:
						to_return.append(ChordInterface.get_chord_name(chord))
			elif index[2] == "m":
				for chord in to_search:
					if chord.quality == "minor" and str.lower(ChordInterface.get_chord_name(chord)).startswith(
							index[0] + index[1]) is True:
						to_return.append(ChordInterface.get_chord_name(chord))

		if len(to_return) == 0:  # only if we don't have any valid chords already
			for chord in to_search:
				if str.lower(ChordInterface.get_chord_name(chord)).startswith(index) is True:
					to_return.append(ChordInterface.get_chord_name(chord))

			if len(to_return) == 0:  # similarity search
				for chord in to_search:
					if SequenceMatcher(None, str.lower(ChordInterface.get_chord_name(chord)), index).ratio() > 0.8:
						to_return.append(ChordInterface.get_chord_name(chord))

				if len(to_return) == 0:  # if it's still 0, lower accuracy
					for chord in to_search:
						if SequenceMatcher(None, str.lower(ChordInterface.get_chord_name(chord)), index).ratio() > 0.75:
							to_return.append(ChordInterface.get_chord_name(chord))

		# searching is done, now prepare the results for being sent to the front-end

		# remove all dupes
		no_dupes_to_return = []
		[no_dupes_to_return.append(x) for x in to_return if x not in no_dupes_to_return]  # Get rid of dupes

		# debug missing chords
		print(f"found chords: {len(no_dupes_to_return)}. before no_dupes: {len(to_return)}")

		return no_dupes_to_return
