from abc import ABC
from abc import abstractmethod


class Instrument(ABC):
	@abstractmethod
	def my_method(self):
		pass
	# TODO
