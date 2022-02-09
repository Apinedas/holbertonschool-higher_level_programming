#!/usr/bin/python3
"""
    Module to test Rectangle class
"""


import unittest
from models.rectangle import Rectangle
from io import StringIO
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):
    """
        Test class for Rectangle class
    """
    def test_rect_1(self):
        rect_test = Rectangle(1, 2)
        self.assertEqual(rect_test.width, 1)
        self.assertEqual(rect_test.height, 2)

    def test_rect_2(self):
        rect_test = Rectangle(1, 2, 3)
        self.assertEqual(rect_test.width, 1)
        self.assertEqual(rect_test.height, 2)
        self.assertEqual(rect_test.x, 3)

    def test_rect_3(self):
        rect_test = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect_test.width, 1)
        self.assertEqual(rect_test.height, 2)
        self.assertEqual(rect_test.x, 3)
        self.assertEqual(rect_test.y, 4)

    def test_rect_3(self):
        rect_test = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect_test.width, 1)
        self.assertEqual(rect_test.height, 2)
        self.assertEqual(rect_test.x, 3)
        self.assertEqual(rect_test.y, 4)
        self.assertEqual(rect_test.id, 5)

    def test_rect_4(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(0, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, -1)

    def test_rect_str(self):
        test_rect = Rectangle(1, 2, 0, 0, 1012)
        ret = "[Rectangle] (1012) 0/0 - 1/2"
        self.assertEqual(str(test_rect), ret)

    def test_rect_display(self):
        test_rect = Rectangle(2, 2)
        ret = "##\n##\n"
        with redirect_stdout(StringIO()) as f:
            test_rect.display()
        s = f.getvalue()
        self.assertEqual(ret, s)

    def test_rect_display_x(self):
        test_rect = Rectangle(2, 2, 2)
        ret = "  ##\n  ##\n"
        with redirect_stdout(StringIO()) as f:
            test_rect.display()
        s = f.getvalue()
        self.assertEqual(ret, s)

    def test_rect_display_xy(self):
        test_rect = Rectangle(2, 2, 2, 2)
        ret = "\n\n  ##\n  ##\n"
        with redirect_stdout(StringIO()) as f:
            test_rect.display()
        s = f.getvalue()
        self.assertEqual(ret, s)

    def test_rect_todictionary(self):
        test_rect = Rectangle(1, 2, 3, 4, 5)
        ret = {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1}
        self.assertEqual(test_rect.to_dictionary(), ret)

if __name__ == '__main__':
    unittest.main()
