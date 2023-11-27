#!/usr/bin/python3
"""
Module for print square method.
"""
def print_square(size):
    """
    This function to print a square.
    Args:
        size: size is the size length of the square.
    raises:
        TypeError: If size not an integer.
        ValueError: If size less than zero.
    """



    if not isinstance(size,int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)

    if __name__ = "__main__":
        import doctest
        doctest.testfile("tests/4-print_square.txt")
