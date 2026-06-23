# test_math_utils_pytest.py
# pytest test suite for math_utils.py
# Install pytest once:  pip install pytest
# Run with:            pytest test_math_utils_pytest.py -v

import pytest
from math_utils import add, is_even, safe_divide, celsius_to_fahrenheit


# --- Tests for add() ---

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_floats():
    assert abs(add(0.1, 0.2) - 0.3) < 1e-5


# --- Tests for is_even() ---

def test_even_number_returns_true():
    assert is_even(10) is True

def test_odd_number_returns_false():
    assert is_even(7) is False


# --- Tests for safe_divide() ---

def test_normal_division():
    assert safe_divide(10, 2) == 5.0

def test_division_by_zero_raises_value_error():
    with pytest.raises(ValueError):
        safe_divide(10, 0)


# --- Parametrised test: run the same test with multiple inputs ---

@pytest.mark.parametrize("celsius, expected_f", [
    (0,    32.0),
    (100,  212.0),
    (-40,  -40.0),   # The one temperature where Celsius equals Fahrenheit
    (37,   98.6),
])
def test_celsius_to_fahrenheit(celsius, expected_f):
    assert abs(celsius_to_fahrenheit(celsius) - expected_f) < 0.1
