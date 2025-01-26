#!/usr/bin/python3
"""
This module provides a function that multiplies 2 matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a: first matrix (list of lists of integers/floats)
        m_b: second matrix (list of lists of integers/floats)

    Returns:
        A new matrix representing the multiplication of m_a by m_b

    Raises:
        ValueError: If matrices can't be multiplied or are empty
        TypeError: If inputs are not valid matrices
    """
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

    try:
        np_a = np.array(m_a)
        np_b = np.array(m_b)
        result = np.matmul(np_a, np_b)
        return result.tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
    except TypeError:
        if not all(isinstance(x, (int, float)) for row in m_a for x in row):
            raise TypeError("m_a should contain only integers or floats")
        if not all(isinstance(x, (int, float)) for row in m_b for x in row):
            raise TypeError("m_b should contain only integers or floats")
        if not all(len(row) == len(m_a[0]) for row in m_a):
            raise TypeError("each row of m_a must be of the same size")
        if not all(len(row) == len(m_b[0]) for row in m_b):
            raise TypeError("each row of m_b must be of the same size")
        raise TypeError("invalid input") 