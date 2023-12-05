#!/usr/bin/python3
"""Defines a function for generating Pascal's Triangle."""


def generate_pascals_triangle(n):
    """Generate Pascal's Triangle of size n.

    Args:
        n (int): The size of the Pascal's Triangle.

    Returns:
        list: A list of lists of integers representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    pascals_triangle = [[1]]
    while len(pascals_triangle) != n:
        current_row = pascals_triangle[-1]
        new_row = [1]
        for i in range(len(current_row) - 1):
            new_row.append(current_row[i] + current_row[i + 1])
        new_row.append(1)
        pascals_triangle.append(new_row)

    return pascals_triangle
