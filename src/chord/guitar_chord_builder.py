import music21
from tools import tree
from common.guitar import guitar
from src.defaults import syn_notes


class GuitarChord:
	def __init__(self, chord, lowest_string, string_holder=None) -> None:
		"""

		:type chord: music21.chord
		:type lowest_string: GuitarString
		"""

		if string_holder is None:
			string_holder = guitar.guitar
		self._string_holder = string_holder

		self._chord = chord
		self._bass = chord.bass
		self._bass_fret = 0
		self._lowest_string = lowest_string
		self._allowed_frets = _get_chord_frets(chord, self._string_holder)

		self._open_fret = 0

		self._thumb = False

	# getters and setters

	@property
	def chord(self):
		return self._chord

	@chord.setter
	def chord(self, chord):
		if type(chord) is music21.chord:
			self._chord = chord
		elif type(chord) is str:
			# Potential bug source, use with care as enharmonics may be generated!
			# Consider linking to the chord generator in the project instead, to avoid enharmonics
			self._chord = music21.chord.Chord(chord)

	# methods

	# TODO: Refactor
	def _get_frets_on_string(self, prev, string, max_add=3, guit=None, bass_fret=None) -> list:
		"""

		:param prev: Previous fret number, int
		:param string: Previous string, not an actual string object, but a list
		:param max_add: Max num to add
		:param guit: Replacement string holder
		:return: List
		"""
		valid_frets = []

		# TODO: Some absurd things can appear, such as 15 2 0 1 0, look into it later
		# todo 2: some chords don't work at all?

		if guit is None:
			guit = self._string_holder
		if bass_fret is None:
			bass_fret = self._bass_fret

		ggs = guit.get_strings()
		if self._thumb and self._lowest_string == ggs[len(ggs) - 1] and max_add > 0:
			max_add -= 1  # Thumb makes stretchy chords harder

		for fret in string:
			fr = fret.get_number()  # todo: refactor and del this line
			num = fret.get_number()

			# Open bass -> Open string
			if bass_fret == self._open_fret and num == self._open_fret:
				valid_frets.append(fret)

			# if the fret is lower than prev and bass
			if fr <= prev and fr <= bass_fret:
				# If it is open
				if fr == self._open_fret:
					valid_frets.append(fret)
					continue

				if fr >= bass_fret - 1 and fr >= prev - 1:
					valid_frets.append(fret)
					continue

			if fr > prev and fr > bass_fret:
				pass  # todo: improve, or rewrite the logic

			if fr <= prev + max_add - 1 and fr <= bass_fret + max_add:
				if (fr >= bass_fret - 1 or fr >= prev - 1) or fr == self._open_fret:
					if fr > bass_fret - (max_add + 1):
						valid_frets.append(fret)
						continue

			if fr <= prev + max_add - 2 and fr <= bass_fret + max_add - 1:
				if fr >= bass_fret - 1 or fr == self._open_fret:
					if fr > bass_fret - (max_add + 1):
						valid_frets.append(fret)
						continue

		# Return muted string if no valid frets are found
		if len(valid_frets) == 0:
			return ["x"]

		return valid_frets

	# Todo: Refactor
	def _check_shape_validity(self, shape) -> bool:
		"""

		:param shape: Shape to check the validity of (list)
		:return: True/False
		"""
		finger_count = 4
		# If we may use the thumb and the thumb can reach
		if self._thumb and self._lowest_string == self._string_holder.get_string_count() - 1:
			finger_count += 1

		free_fingers = 0
		can_bar = False
		bar1 = 0
		bar2 = 0
		prev_fret = None
		prev_row = 0
		unchecked_notes = self._chord.notes

		# todo: potentially split up into smaller methods

		lowest = None
		for item in shape:
			if type(item) != str and lowest is None:
				lowest = item.get_number()
			elif type(item) == str:
				continue
			if item.get_number() < lowest:
				lowest = item.get_number()

		highest_fret = None
		for item in shape:
			if type(item) != str and highest_fret is None:
				highest_fret = item.get_number()
			elif type(item) == str:
				continue
			if item.get_number() > highest_fret:
				highest_fret = item.get_number()

		lowest_non_open = None
		for item in shape:
			if type(item) != str and lowest_non_open is None:
				lowest_non_open = item.get_number()
			elif type(item) == str:
				continue
			if item.get_number == self._open_fret:
				continue
			if item.get_number() < lowest_non_open:
				lowest_non_open = item.get_number()

		# Check if its possible to bar (1)
		if self._bass_fret > 0:
			if lowest != self._open_fret and lowest == self._bass_fret:
				can_bar = True

			for fret_ in shape:
				fret = fret_
				if type(fret_) != str:
					fret = fret_.get_number()
				if fret_ == prev_fret and can_bar:
					prev_row += 1
					if prev_row >= 3:
						bar1 = prev_row
				prev_fret = fret

			# Check for a 2nd bar (ex A shape bars)
			# Todo

		for fret_ in shape:
			fret = fret_
			note = None
			if type(fret_) != str:
				fret = fret_.get_number()
				note = fret_.get_note_name()

			# First, check if all the notes of the chord are actually in it!
			if note in unchecked_notes:
				unchecked_notes.remove(note)

			if fret != "x":
				free_fingers -= 1

		# Check for unreasonable stretches, such as x x 4 6 0 1
		if highest_fret - lowest_non_open >= 4:
			return False

		# Count fingers TODO

		# There are notes that should be in the chord that are not there!
		if len(unchecked_notes) > 0:
			return False

		return True

	def get_shapes(self, inversion=False) -> list:
		"""
		Gets *all* valid chord shapes for a given chord, matching specified criteria.

		Tries to find all valid frets (using _get_chord_frets) and then uses tree structures to
		find chord shapes.

		:param inversion: If the chord is allowed to be an inversion or not
		:return: List of all valid shapes for the chord
		"""
		shapes_to_ret = []
		lowest = self._lowest_string

		# Prevent annoying errors that may result from some genius inputting
		# lowest_string > len(strings) or other high numbers
		if self._string_holder.get_string_count() - 1 - lowest < 0:
			print("Invalid lowest string")
			return []

		# Select the bass string
		selected_string = self._allowed_frets[lowest]
		# if the line above errors it's because of either:
		# 1. Bug with _get_chord_frets()
		# 2. Invalid string holder

		# With the bass string selected we now loop through its frets, to find the bass fret
		# It may be possible to find multiple bass frets, and valid sets of shapes will be returned for
		# all of them.
		for fret in selected_string:
			if fret.get_note_name() == self._chord.root().name and inversion is False and \
				fret.get_number() >= self._open_fret:
				bass_fret = fret
			elif inversion and fret.get_number() >= self._open_fret:
				bass_fret = fret
			else:
				continue

			self._bass_fret = bass_fret.get_number()

			# Set up the tree for the chords, with the bass_fret as the root
			chord_tree = tree.Tree(bass_fret)

			# With the bass fret set up and all that, we find the children for it.
			first_children = self._get_frets_on_string(
				bass_fret.get_number(),  # Prev
				self._allowed_frets[lowest - 1]  # String
			)

			for child in first_children:
				chord_tree.add_child(child)

			# the tree should now have its first children, and we can go through those children and add even more
			# i should be lowest - 2 since we have already went through 2 of the strings.
			n = lowest - 2
			i = 0
			while n >= 0:
				next_string = self._allowed_frets[n]

				nodes = tree.get_nodes_at_depth(chord_tree, i + 1)

				prev_node_data = None
				for node in nodes:
					if node.data != "x":
						for node_child in self._get_frets_on_string(node.data.get_number(), next_string):
							node.add_child(node_child)
							prev_node_data = node.data

					elif prev_node_data is not None:
						for node_child in self._get_frets_on_string(prev_node_data.get_number(), next_string):
							node.add_child(node_child)

				n -= 1
				i += 1

			# Sum up the branches to create shapes
			for end_node in tree.get_end_nodes(chord_tree):
				new_res = [item for item in tree.get_branch_items(end_node)]
				while len(new_res) < self._string_holder.get_string_count():
					new_res.append("x")
				new_res = new_res[::-1]

				if self._check_shape_validity(new_res):
					shapes_to_ret.append(new_res)
					msg = ""
					for x in new_res:
						if x != "x":
							msg += str(x.get_number())
						else:
							msg += "x"
						msg += " "
					print(msg)

		return shapes_to_ret


def _get_chord_frets(chord, string_holder=None) -> list:
	"""
	This abomination of function takes a chord, and then returns all the valid frets for that chord
	in a list format, somehow. How it works is a secret that no-one knows, it just works.
	A valid fret is a fret that contains a note that is inside the chosen chord.
	:param chord: music21 chord object
	:param string_holder: If you wish to override the default string set
	:return: A list with "strings" that also contains frets.
	"""
	new_strings = []

	if string_holder is None:
		string_holder = guitar.guitar
	strings = string_holder.get_strings()

	def is_syn(note_a, note_b) -> bool:
		return syn_notes.syn_notes.is_syn_note(note_a, note_b)

	for string in strings:
		new_strings.append(
			[
				# get notes from the chord, check if their names match the fret names
				n for n in string.get_frets() if any([is_syn(x, n.get_note()) for x in chord.notes])
			]
		)

	return new_strings


def get_lowest(shapes) -> list:
	if len(shapes) == 0:
		return []
	lowest = shapes[0]
	for shape in shapes:
		for i in range(len(shape)):
			if shape[i] == "x":
				break
			if lowest[i] == "x":
				lowest = shape
			if shape[i] < lowest[i]:
				lowest = shape
			elif shape[i] > lowest[i]:
				break
	return lowest
