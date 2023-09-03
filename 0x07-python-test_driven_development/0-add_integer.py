#!/usr/bin/python3
# 0-add_integer.py

def add_integer(a, b=98):
    """
    Return the integer addition of a and b.

    Float arguments are cast to ints before addition is performed.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The integer sum of a and b.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both a and b must be integers or floats")
    return int(a) + int(b)
