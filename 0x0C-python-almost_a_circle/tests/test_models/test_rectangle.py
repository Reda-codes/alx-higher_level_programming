#!/usr/bin/python3
"""Unittests for base
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """unit test for Rectangle model"""

    def test_initialization(self):
        re1 = Rectangle(4,8)
        self.assertEqual(re1.id, Rectangle._Base__nb_objects)
        re2 = Rectangle(2,4)
        self.assertEqual(re2.id, Rectangle._Base__nb_objects)


if __name__ == '__main__':
    unittest.main()
