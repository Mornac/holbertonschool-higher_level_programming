#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_integer(self):
        self.assertIsNone(max_integer([]))

    def test_zero_integer(self):
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_positive_integer(self):
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integer(self):
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_integer(self):
        self.assertEqual(max_integer([1, -2, 3]), 3)
        self.assertEqual(max_integer([-1, 2, -3]), 2)
        self.assertEqual(max_integer([-1, -2, 0]), 0)

    def test_float_integer(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([1.5, -2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([-1.5, -2.5, -3.5]), -1.5)

    def test_identical_integer(self):
        self.assertEqual(max_integer([1, 1, 1]), 1)
        self.assertEqual(max_integer([2, 2, 2]), 2)
        self.assertEqual(max_integer([-1, -1, -1]), -1)

    def test_identical_float_integer(self):
        self.assertEqual(max_integer([1.5, 1.5, 1.5]), 1.5)
        self.assertEqual(max_integer([2.5, 2.5, 2.5]), 2.5)
        self.assertEqual(max_integer([-1.5, -1.5, -1.5]), -1.5)

    def test_identical_mixed_integer(self):
        self.assertEqual(max_integer([1, 1.5, 1]), 1.5)
        self.assertEqual(max_integer([2, 2.5, 2]), 2.5)
        self.assertEqual(max_integer([-1, -1.5, -1]), -1)

    def test_large_list(self):
        self.assertEqual(max_integer([1] * 1000), 1)
        self.assertEqual(max_integer([2] * 1000), 2)
        self.assertEqual(max_integer([-1] * 1000), -1)

    def test_large_integer(self):
        self.assertEqual(max_integer([1000000, 2000000, 3000000]), 3000000)
        self.assertEqual(max_integer([1000000, -2000000, 3000000]), 3000000)
        self.assertEqual(max_integer([-1000000, -2000000, -3000000]), -1000000)

    def test_string_integer(self):
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')
        with self.assertRaises(TypeError):
            max_integer(['a', 'b', 'c', 1])
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, 'a'])
        with self.assertRaises(TypeError):
            max_integer(['a', 1, 2])

    def test_tuple_integer(self):
        self.assertEqual(max_integer((1, 2, 3)), 3)
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)
        self.assertEqual(max_integer((1, 2, 3, -4)), 3)
        self.assertEqual(max_integer((-1, -2, -3)), -1)

    def test_list_integer(self):
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
