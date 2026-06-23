# test_math_utils.py
# unittest test suite for math_utils.py
# Run with:  python test_math_utils.py

import unittest
from math_utils import add, is_even, safe_divide, celsius_to_fahrenheit

 
class TestAdd(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_with_zero(self):
        self.assertEqual(add(0, 100), 100)

    def test_add_floats(self):
        # assertAlmostEqual avoids floating-point precision failures
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=5)


class TestIsEven(unittest.TestCase):

    def test_even_number_returns_true(self):
        self.assertTrue(is_even(10))

    def test_odd_number_returns_false(self):
        self.assertFalse(is_even(7))

    def test_zero_is_even(self):
        self.assertTrue(is_even(0))

    def test_negative_even(self):
        self.assertTrue(is_even(-4))


class TestSafeDivide(unittest.TestCase):

    def test_normal_division(self):
        self.assertEqual(safe_divide(10, 2), 5.0)

    def test_division_by_zero_raises_value_error(self):
        # assertRaises checks that the expected exception IS raised
        with self.assertRaises(ValueError):
            safe_divide(10, 0)


class TestCelsiusToFahrenheit(unittest.TestCase):

    def test_freezing_point(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_boiling_point(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_body_temperature(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6, places=1)


if __name__ == "__main__":
    unittest.main()
