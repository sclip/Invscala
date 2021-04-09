from src.data.defaults import syn_notes, chord_shapes as chs, default
import eel
from common.guitar import guitar_string
from src.connect.html_builder import build_helper
from src.data.chord import chord_fixer
from src.tools import list_methods


class Guitar:
	def __init__(self, testing=False):
		# load settings
		if testing is False and default.settings.loaded_settings is True:
			self.__lowest_fret = 0
			self.__highest_fret = default.settings.get_setting("guitar", "Default Highest Fret")

			self.__maximum_fret = default.settings.get_setting("guitar", "Default Maximum Fret")

			self.__string_count = default.settings.get_setting("guitar", "Default String Count")
			self.__min_strings = default.settings.get_setting("guitar", "Minimum String Count")
			self.__max_strings = default.settings.get_setting("guitar", "Maximum String Count")
			self.__string_names = default.settings.get_setting("guitar", "String Names")
			self.__string_notes = default.settings.get_setting("guitar", "String Notes")
		elif testing is True:
			self.__lowest_fret = 0
			self.__highest_fret = 24

			self.__maximum_fret = 36

			self.__string_count = 6
			self.__min_strings = 1
			self.__max_strings = 9
			self.__string_names = ["e", "B", "G", "D", "A", "E"]
			self.__string_notes = ["E4", "B3", "G3", "D3", "A2", "E2"]
		else:
			self.__lowest_fret = 0
			self.__highest_fret = 24

			self.__maximum_fret = 36

			self.__string_count = 6
			self.__min_strings = 1
			self.__max_strings = 9
			self.__string_names = ["e", "B", "G", "D", "A", "E"]
			self.__string_notes = ["E4", "B3", "G3", "D3", "A2", "E2"]

		self.strings = []

	def load(self):
		self.__lowest_fret = 0
		self.__highest_fret = int(default.settings.get_setting("guitar", "Default Highest Fret")) + 1

		self.__maximum_fret = default.settings.get_setting("guitar", "Default Maximum Fret") + 1

		self.__string_count = default.settings.get_setting("guitar", "Default String Count")
		self.__min_strings = default.settings.get_setting("guitar", "Minimum String Count")
		self.__max_strings = default.settings.get_setting("guitar", "Maximum String Count")
		self.__string_names = default.settings.get_setting("guitar", "String Names")
		self.__string_notes = default.settings.get_setting("guitar", "String Notes")

		self.generate_strings()

	def generate_strings(self):
		for i in range(self.__string_count):
			self.strings.append(guitar_string.generate_string(
				self.__string_names[i],
				self.__lowest_fret,
				self.__highest_fret,
				starting_note=self.__string_notes[i],
				num=i
			))

	def get_string_by_id(self, id_):
		return self.strings[id_]

	def get_strings(self):  # string[0] is always the high E! String[5] for low E
		return self.strings

	def get_string_count(self):
		return self.__string_count

	def build(self):
		build_helper.build_fret_numbering(self.__highest_fret)
		build_helper.build_string(self.__string_count)
		for string in self.strings:
			build_helper.build_frets(self.__highest_fret, string, self.strings.index(string))
		build_helper.build_string_selection(self.__min_strings, self.__max_strings, self.__string_count)

	def get_lowest_chord(self, chord):
		frets = []
		dn_1 = False
		for i in range(5):
			for n in range(3, 6)[::-1]:
				if self.strings[n].get_frets()[i].get_note_name() == chord.root().name:
					if n != 5:
						frets.append("x")
					frets.append(i)
					dn_1 = True
					break
			if dn_1 is True:
				break

			# if self.strings[4].get_frets()[i].get_note_name() == chord.root().name and len(frets) == 0:
			#    print("hello2")
			#    frets.append("x")
			#    frets.append(i)

			# if self.strings[3].get_frets()[i].get_note_name() == chord.root().name and len(frets) == 0:
			#    print("hello3")
			#    frets.append("x")
			#    frets.append(i)

		if len(frets) == 0:
			print("???")
		else:
			frets_len = len(frets)
			while frets_len < 6:
				found = False

				frets_ = self.strings[5 - frets_len].get_frets()

				if frets_len < 2 and frets[0] != "x":
					pitches = [chord.third, chord.fifth, chord.seventh]
				elif frets_len < 2 and frets[0] == "x":
					pitches = [chord.third, chord.fifth, chord.seventh]
				elif frets_len < 3 and frets[1] == "x":
					pitches = [chord.third, chord.fifth, chord.seventh]
				else:
					pitches = [chord.root(), chord.third, chord.fifth, chord.seventh]
				pitch_names = []
				for pitch in pitches:
					if pitch is not None:
						pitch_names.append(pitch.name)

				if frets_[0].get_note_name() in pitch_names:
					frets.append(frets_.index(frets_[0]))
					found = True

				elif frets[-1] != "x":
					if frets[-1] > 1:
						for i in range(frets[-1] + 2):

							if frets_[i].get_note_name() in pitch_names:
								frets.append(frets_.index(frets_[i]))
								found = True
					elif frets[-1] > 2:
						for i in range(frets[-1] - 1, frets[-1] + 2):

							if frets_[i].get_note_name() in pitch_names:
								frets.append(frets_.index(frets_[i]))
								found = True
					elif frets[-1] == 0:
						for i in range(4):

							if frets_[i].get_note_name() in pitch_names:
								frets.append(frets_.index(frets_[i]))
								found = True
					else:
						for i in range(frets[-1] + 3):

							if frets_[i].get_note_name() in pitch_names:
								frets.append(frets_.index(frets_[i]))
								found = True

				elif frets[frets_len - 2] != "x":

					for i in range(frets[frets_len - 2] + 2):

						if frets_[i].get_note_name() in pitch_names:
							frets.append(frets_.index(frets_[i]))
							found = True

				# for note in self.strings[5-frets_len].get_frets():
				#     pitches = [chord.third, chord.fifth, chord.seventh]
				#     pitch_names = []
				#     for pitch in pitches:
				#         if pitch is not None:
				#             pitch_names.append(pitch.name)
				#     if note.get_note_name() in pitch_names:
				#         i = self.strings[5-frets_len].get_index_of_note(note)
				#         if frets[-1] != "x":
				#             if i < frets[-1] + 3:
				#                 frets.append(i)
				#                 found = True
				if found is False:
					frets.append("x")
					print("adding x")
				frets_len = len(frets)

		return frets

	def get_lowest_caged_chord(self, chord, caged_chords=None):
		if caged_chords is None:
			caged_chords = chs.chord_shapes.get_chord_shapes()
		chord_frets = []
		# Get root note on the 3 first strings
		s = syn_notes.syn_notes.is_syn_note
		for n in range(3, 6)[::-1]:
			for i in range(12):
				if s(self.strings[n].get_fret(i).get_note(), chord.root()):
					# if n != 5:
					#     chord_frets.append(-1)
					chord_frets.append(i)
		print(chord_frets)
		# Compare to find the lowest
		lowest = chord_frets.index(list_methods.get_lowest_item(chord_frets))
		print(lowest)
		# Knowing the lowest string to use, we can choose what chord type. It'll be E, A or D
		chord_shapes = ["E", "A", "D"]
		chord_shape = caged_chords[chord_fixer.get_real_chord_quality(chord)][chord_shapes[lowest]]
		print(chord_shape)
		# Now we transpose this shape up to where we need it. Extra attention is paid to avoid errors with "x"
		# The distance we need to transpose is easy to figure out, as we know the fret #
		new_shape = []
		for fret in chord_shape:
			if fret != "x":
				new_shape.append(chord_frets[lowest] + fret)
			else:
				new_shape.append("x")
		print(new_shape)
		return new_shape


# If this is loaded outside of the main running process then settings will likely not be set up properly
# Create a new guitar object with the flag Testing=True instead!
guitar = Guitar()


@eel.expose
def reset_select_guitar():
	for string in guitar.get_strings():
		for fret_ in string.get_selected_frets():
			string.select_fret(fret_.get_number())
	eel.deselect_all_frets()


@eel.expose
def full_reset_highlight():
	for string in guitar.get_strings():
		guitar_string.reset_highlight(string)
	eel.deselect_all_frets()
