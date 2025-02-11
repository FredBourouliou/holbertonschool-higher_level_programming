#!/usr/bin/python3
"""Module for Pascal's Triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n"""
    if n <= 0:
        return []

    triangles = [[1]]
    for i in range(n - 1):
        tri = triangles[-1]
        tmp = [1]
        for j in range(len(tri) - 1):
            tmp.append(tri[j] + tri[j + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
