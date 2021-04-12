from src.connect.command.display_notes import display_notes


class GuitarChord(display_notes.DisplayNotes):
	""" Displays a guitar chord """

	def __init__(self, notes):
		super(GuitarChord, self).__init__(notes, "guitar")
