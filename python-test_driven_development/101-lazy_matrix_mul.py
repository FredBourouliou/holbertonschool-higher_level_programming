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
    try:
        return np.matmul(m_a, m_b).tolist()
    except ValueError as e:
        if "shapes" in str(e):
            raise ValueError("m_a and m_b can't be multiplied")
        raise ValueError("empty matrices")
    except TypeError as e:
        if "list" in str(e):
            raise TypeError("m_a must be a list or m_b must be a list")
        raise TypeError("invalid input") 