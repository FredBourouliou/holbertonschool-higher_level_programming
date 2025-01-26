#!/usr/bin/python3
"""
This module provides a function that multiplies 2 matrices using NumPy.
"""
try:
    import numpy as np
except ImportError:
    print("numpy module not found. Please install it using: pip3 install numpy==1.15.0")
    exit(1)


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
        result = np.matmul(m_a, m_b)
        return str(result)
    except ValueError as e:
        if "shapes" in str(e):
            raise ValueError("shapes not aligned")
        raise ValueError(str(e))
    except TypeError as e:
        if "scalar" in str(e):
            raise TypeError("Scalar operands are not allowed, use '*' instead")
        raise TypeError(str(e)) 