""" Fret object """


class Fret:
	def __init__(self, string, no, note):
		self.__number = no
		self.__string = string
		self.__name = string + str(no)
		self.__note = note

	def get_note(self):
		return self.__note

	def get_note_name(self):
		return self.__note.name

	def get_number(self):
		return self.__number

	def get_name(self):
		return self.__name

	def transpose(self, semitones, in_place=True):
		self.__note.transpose(semitones, inPlace=in_place)
