#!/usr/bin/python3
"""
    Module to test Rectangle class
"""


import unittest
from models.rectangle import Rectangle


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

if __name__ == '__main__':
    unittest.main()
