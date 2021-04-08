import music21
from common.guitar import fret


class GuitarString:  # prob don't want to name this "String"
	def __init__(self, frets, name, number=0):
		self.__frets = frets  # list

		self.__base_note = music21.note.Note(name)
		self.__def_note = music21.note.Note(name)

		self.__name = name[0]
		if int(self.__def_note.octave) >= 4:
			self.__name = str.casefold(self.__name)

		self.__def_name = self.__name
		self.__long_name = f"{self.__name} String"
		self.__number = 0

		self.__highlighted_frets = []
		self.__selected_frets = []

		self.__tuning_distance = 0

	def get_name(self):
		return self.__name

	def get_long_name(self):
		return self.__long_name

	def get_number(self):
		return self.__number

	def get_frets(self):  # returns a list
		return self.__frets

	def get_fret(self, nr):
		return self.__frets[nr]

	def get_selected_frets(self):
		return self.__selected_frets

	def get_highlighted_frets(self):
		return self.__highlighted_frets

	def select_fret(self, fret_nr):
		try:
			if self.__frets[fret_nr] in self.__selected_frets:
				self.__selected_frets.remove(self.__frets[fret_nr])
				print(f"deselected fret {fret_nr}")
				print(self.__selected_frets)
			else:
				self.__selected_frets.append(self.__frets[fret_nr])
				print(f"selected fret {fret_nr}")
				print(self.__selected_frets)
		except IndexError:
			print(f"No such fret on string {self.__name}; {fret_nr}")

	def highlight_fret(self, fret_id):
		try:
			fret_ = self.get_fret(fret_id)
		except IndexError:
			return
		if fret_ not in self.__highlighted_frets:
			self.__highlighted_frets.append(fret_)
		elif fret_ in self.__highlighted_frets:
			self.__highlighted_frets.remove(fret_)

	def change_tuning(self, semitones):
		self.__highlighted_frets = []
		self.__selected_frets = []

		self.__base_note.transpose(semitones)
		self.__name = self.__base_note.name
		self.__tuning_distance += semitones  # some sort of memory for reset tuning
		for fret_ in self.__frets:
			fret_.transpose(semitones)  # could have frets be a stream instead and transpose the stream, but this works

	def reset_tuning(self):
		self.__name = self.__def_name
		self.__base_note = self.__def_note

		if self.__tuning_distance == 0:
			return
		elif self.__tuning_distance < 0:
			while self.__tuning_distance < 0:
				self.change_tuning(1)
		else:
			while self.__tuning_distance > 0:
				self.change_tuning(-1)

	def get_index_of_note(self, to_index):
		new_string = [x.get_note_name() for x in self.get_frets()]
		return new_string.index(to_index.get_note_name())


# # # INTERFACE # # #
# an attempt to ditch static classes as interfaces seen in previous modules here

def get_notes(string):
	new_frets = []
	for fret_ in string.get_frets():
		new_frets.append(fret_.get_note())
	return new_frets


def reset_highlight(string):
	for fret_ in string.get_highlighted_frets():
		string.highlight_fret(fret_.get_number())


def generate_string(string_name, lowest_fret, highest_fret, starting_note="E4", num=0):
	string_content = []
	starting_note_ = music21.note.Note(starting_note)
	for fr_nr in range(lowest_fret, highest_fret):
		note = starting_note_.transpose(fr_nr)
		new_fret = fret.Fret(string_name, fr_nr, note)
		string_content.append(new_fret)
	return GuitarString(string_content, starting_note, num)
