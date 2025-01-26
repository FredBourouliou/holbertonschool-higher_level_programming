#!/usr/bin/python3
"""
This module provides a function that multiplies 2 matrices.
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a: first matrix (list of lists of integers/floats)
        m_b: second matrix (list of lists of integers/floats)

    Returns:
        A new matrix representing the multiplication of m_a by m_b

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                  contains non-numbers, or is not rectangular
        ValueError: If m_a or m_b is empty or can't be multiplied
    """
    if m_a is None or m_b is None:
        raise TypeError("matrix_mul() missing 2 required positional arguments: \
'm_a' and 'm_b'")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    row_size_a = len(m_a[0])
    row_size_b = len(m_b[0])

    if not all(len(row) == row_size_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == row_size_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(round(element, 2))
        result.append(row)

    return result
