from src.connect.command import command
import eel


class DisplayNotes(command.Command):
	def __init__(self, notes, receiver):
		self._notes = notes
		self._receiver = receiver

	def execute(self) -> None:
		eel.displayNotes(self._notes, self._receiver)
