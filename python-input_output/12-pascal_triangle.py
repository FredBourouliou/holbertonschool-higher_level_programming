#!/usr/bin/python3
"""
Module for Pascal's Triangle function
Returns a list of lists of integers representing Pascal's triangle
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n

    Args:
        n (int): number of rows of Pascal's triangle to calculate

    Returns:
        list: empty list if n <= 0
             list of lists of integers representing Pascal's triangle of n
    """
    if n <= 0:
        return []

    triangles = [[1]]
    for i in range(n - 1):
        tri = triangles[-1]  # Get the last row
        tmp = [1]  # First element is always 1
        for j in range(len(tri) - 1):
            tmp.append(tri[j] + tri[j + 1])  # Sum of the two numbers above
        tmp.append(1)  # Last element is always 1
        triangles.append(tmp)
    return triangles
