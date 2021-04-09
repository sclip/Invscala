from abc import ABC
from abc import abstractmethod


class Instrument(ABC):
	@abstractmethod
	def load(self):
		pass
