from src.data.instrument.guitar import guitar


class InstrumentSelector:
	def __init__(self, instrument) -> None:
		self._instrument = instrument

	@property
	def instrument(self):
		return self._instrument

	@instrument.setter
	def instrument(self, value):
		self._instrument = value

	def operation(self):
		# self._subsystem.operation()
		pass


def select_instrument(selection):
	# Todo: With py 3.10 use match statement
	if selection == "Guitar":
		return InstrumentSelector(guitar.guitar)
