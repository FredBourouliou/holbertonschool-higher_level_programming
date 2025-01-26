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
    # Check if matrices are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if matrices are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if matrices are empty
    if m_a == [] or m_a == [[]] or not m_a:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]] or not m_b:
        raise ValueError("m_b can't be empty")

    # Check if elements are numbers
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # Check if rows are same size
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    try:
        result = np.matmul(np.array(m_a), np.array(m_b))
        return result.tolist()
    except Exception:
        raise ValueError("m_a and m_b can't be multiplied") 