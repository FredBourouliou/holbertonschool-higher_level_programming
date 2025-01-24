#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix: A list of lists of integers or floats
        div: Number to divide matrix elements by (integer or float)

    Returns:
        A new matrix with all elements divided by div,
        rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                  if rows are not the same size, or if div is not a number
        ZeroDivisionError: If div is zero
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(err_msg)

    if not all(
            isinstance(num, (int, float))
            for row in matrix for num in row):
        raise TypeError(err_msg)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if div == float('inf') or div == float('-inf'):
        return [[0.0 for num in row] for row in matrix]

    return [[round(num / div, 2) for num in row] for row in matrix]
