#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def empty_integer(self):
        self.assertEqual(max_integer([]), None)

    def zero_integer(self):
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def positive_integer(self):
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def negative_integer(self):
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def mixed_integer(self):
        self.assertEqual(max_integer([1, -2, 3]), 3)
        self.assertEqual(max_integer([-1, 2, -3]), 2)
        self.assertEqual(max_integer([-1, -2, 0]), 0)

    def float_integer(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([1.5, -2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([-1.5, -2.5, -3.5]), -1.5)

    def string_integer(self):
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')
        self.assertEqual(max_integer(['a', 'b', 'c', 1]), TypeError)
        self.assertEqual(max_integer([1, 2, 3, 'a']), TypeError)

    def tuple_integer(self):
        self.assertEqual(max_integer((1, 2, 3)), 3)
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)
        self.assertEqual(max_integer((1, 2, 3, -4)), 3)
        self.assertEqual(max_integer((-1, -2, -3)), -1)

    def list_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def dict_integer(self):
        self.assertEqual(max_integer({'a': 1, 'b': 2, 'c': 3}), 3)
        self.assertEqual(max_integer({'a': 1, 'b': 2, 'c': -3}), 2)
        self.assertEqual(max_integer({'a': -1, 'b': -2, 'c': -3}), -1)
        self.assertEqual(max_integer({'a': 1, 'b': 2, 'c': 3, 'd': 4}), 4)
        self.assertEqual(max_integer({'a': 1, 'b': 2, 'c': 3, 'd': -4}), 3)
        self.assertEqual(max_integer({'a': -1, 'b': -2, 'c': -3, 'd': -4}), -1)
