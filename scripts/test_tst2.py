import unittest
import tst2


class TestTree(unittest.TestCase):
    def test(self):
        ran = [0, 1, 2, 3]
        a = [n[1] for n in tst2.get_frets_on_string(tst2.strings[0][0], tst2.strings[0][0], tst2.strings[1])]
        self.assertEqual(a, ran)
        a = [n[1] for n in tst2.get_frets_on_string(tst2.strings[1][0], tst2.strings[1][0], tst2.strings[2])]
        self.assertEqual(a, ran)
        a = [n[1] for n in tst2.get_frets_on_string(tst2.strings[2][0], tst2.strings[0][0], tst2.strings[3])]
        self.assertEqual(a, ran)
        a = [n[1] for n in tst2.get_frets_on_string(tst2.strings[3][0], tst2.strings[1][0], tst2.strings[4])]
        self.assertEqual(a, ran)

        a = [n[1] for n in tst2.get_frets_on_string(tst2.strings[0][0], tst2.strings[1][0], tst2.strings[2])]
        self.assertEqual(a, ran)

        a = [n[1] for n in tst2.get_frets_on_string(tst2.strings[0][0], tst2.strings[1][1], tst2.strings[2])]
        self.assertEqual(a, [0, 1, 2, 3])

        a = [n[1] for n in tst2.get_frets_on_string(tst2.strings[0][0], tst2.strings[1][2], tst2.strings[2])]
        self.assertEqual(a, [0, 1, 2, 3, 4])

        a = [n[1] for n in tst2.get_frets_on_string(tst2.strings[0][0], tst2.strings[1][1], tst2.strings[2])]
        self.assertEqual(a, [0, 1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
