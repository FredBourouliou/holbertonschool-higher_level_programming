#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_duplicate_numbers(self):
        """Test with duplicate numbers"""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([1, 2, 2, 1]), 2)
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_floats(self):
        """Test with floating point numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)
        self.assertEqual(max_integer([1.0, 2.0, 3.0, 4.0]), 4.0)
        self.assertEqual(max_integer([-1.5, -2.5, -3.5, -4.5]), -1.5)

    def test_mixed_numbers(self):
        """Test with mixed integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)
        self.assertEqual(max_integer([1.5, 2, 3.5, 4]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test with a single element"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)
        self.assertEqual(max_integer([0]), 0)

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([1000000, 2000000, 3000000]), 3000000)
        self.assertEqual(max_integer([-1000000, -2000000, -3000000]), -1000000)

    def test_zero(self):
        """Test with zero"""
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([-1, -2, 0]), 0)

    def test_type_error(self):
        """Test that TypeError is raised when necessary"""
        with self.assertRaises(TypeError):
            max_integer([1, "string", 3])
        with self.assertRaises(TypeError):
            max_integer([1, [2, 3], 4])
        with self.assertRaises(TypeError):
            max_integer([1, None, 3])


if __name__ == '__main__':
    unittest.main()
