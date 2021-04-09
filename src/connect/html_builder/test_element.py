import unittest
from element import *


class ElementTest(unittest.TestCase):
    def test_basic_init(self):
        p = Element("p")
        self.assertEqual(p.get_element(), "<p></p>")

    def test_id_init(self):
        p = Element("p", elem_id="my_paragraph")
        self.assertEqual(p.get_element(), '<p id="my_paragraph"></p>')

    def test_class_init(self):
        p = Element("p", elem_class="paragraphs")
        self.assertEqual(p.get_element(), '<p class="paragraphs"></p>')

    def test_both_init(self):
        p = Element("p", elem_id="my_paragraph", elem_class="paragraphs")
        self.assertEqual(p.get_element(), '<p id="my_paragraph" class="paragraphs"></p>')

    def test_attr_init(self):
        p = Element("p", attr=['style="margin-left: 50px;"'])
        self.assertEqual(p.get_element(), '<p style="margin-left: 50px;"></p>')

        div = Element("div", attr=['style=""', 'id=""'])
        self.assertEqual(div.get_element(), '<div style="" id=""></div>')

    def test_add_content(self):
        p = Element("p")
        p.add_content("abc")
        self.assertEqual(p.get_element(), "<p>abc</p>")


if __name__ == '__main__':
    unittest.main()
