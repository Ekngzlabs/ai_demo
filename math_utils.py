"""
math_utils — Basic mathematical utility functions.

This module provides helper functions for common arithmetic operations
and temperature conversions, with input validation.

Typical usage:
    from math_utils import add, celsius_to_fahrenheit
    total = add(10, 20)
    temp_f = celsius_to_fahrenheit(37)
"""


def add(a: float, b: float) -> float:
    """
    Return the arithmetic sum of a and b.

    Args:
        a (float): First operand.
        b (float): Second operand.

    Returns:
        float: The sum a + b.

    Examples:
        >>> add(2, 3)
        5
        >>> add(-1.5, 1.5)
        0.0
    """
    return a + b

 
def is_even(n: int) -> bool:
    """
    Return True if n is even, False otherwise.

    Args:
        n (int): The integer to test.

    Returns:
        bool: True when n is divisible by 2.

    Examples:
        >>> is_even(4)
        True
        >>> is_even(7)
        False
    """
    return n % 2 == 0


def safe_divide(a: float, b: float) -> float:
    """
    Divide a by b.

    Args:
        a (float): Numerator.
        b (float): Denominator. Must not be zero.

    Returns:
        float: The quotient a / b.

    Raises:
        ValueError: If b is zero.

    Examples:
        >>> safe_divide(10, 2)
        5.0
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def celsius_to_fahrenheit(c: float) -> float:
    """
    Convert a temperature from Celsius to Fahrenheit.

    Args:
        c (float): Temperature in degrees Celsius.

    Returns:
        float: Equivalent temperature in degrees Fahrenheit.

    Examples:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    return c * 9 / 5 + 32

help(celsius_to_fahrenheit)