#!/usr/bin/python3
"""
    Module test for base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """
        Test class for Base class
    """
    base = Base()

    def test_base(self):
        self.assertEqual(self.base.id, 1)

if __name__ == '__main__':
    unittest.main()