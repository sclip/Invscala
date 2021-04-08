import unittest
from testing_file import *


base = 0


sample = [
	[0, 0, 0, 0, 0, 0],
	[0, 1, 2, 3, 4, 5],
	[5, 4, 3, 2, 1, 0],
	[0, 1, 1, 1, 0, 1],
	[0, 0, 0, 1, 1, 1],
	["x", 0, 2, 2, 2, 0],
	["x", 2, 4, 4, 4, 2],
	["x", 3, 3, 3, 3, 3],
	["x", 3, 5, 5, 4, 3],
	[3, 5, 5, 4, 3, 3]
]

sample2 = [
	False,
	False,
	False,
	False,
	True,
	True,
	True,
	True,
	True,
	True
]


class TestCase(unittest.TestCase):
	def test(self):
		i = 0
		for a in sample:
			self.assertEqual(can_bar(base, a), sample2[i])
			i += 1


if __name__ == '__main__':
	unittest.main()
