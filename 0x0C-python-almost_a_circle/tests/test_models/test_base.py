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
    base_1 = Base()
    base_2 = Base()

    def test_base_create(self):
        """
            First test
        """
        self.assertEqual(self.base_1.id, 1)
    
    def test_base_update_id(self):
        self.assertEqual(self.base_2.id, 2)


if __name__ == '__main__':
    unittest.main()
