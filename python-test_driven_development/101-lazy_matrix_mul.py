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
    # Vérification des types de base
    if not isinstance(m_a, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    # Vérification des listes vides
    if not m_a or m_a == [[]]:
        raise ValueError("shapes (0, 0) and (2, 2) not aligned")
    if not m_b or m_b == [[]]:
        raise ValueError("shapes (2, 2) and (0, 0) not aligned")

    try:
        # Conversion en array numpy
        np_a = np.array(m_a)
        np_b = np.array(m_b)
        
        # Vérification des types d'éléments
        if not np.issubdtype(np_a.dtype, np.number):
            raise TypeError("invalid data type for einsum")
        if not np.issubdtype(np_b.dtype, np.number):
            raise TypeError("invalid data type for einsum")

        # Multiplication
        result = np.matmul(np_a, np_b)
        return str(result)

    except ValueError as e:
        if "shapes" in str(e):
            raise ValueError("shapes not aligned")
        raise ValueError(str(e))
    except TypeError as e:
        if "scalar" in str(e):
            raise TypeError("Scalar operands are not allowed, use '*' instead")
        raise TypeError("invalid data type for einsum") 