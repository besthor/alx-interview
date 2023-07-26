#!/usr/bin/python3
"""Writing a function for Pascal's Triangle"""


def pascal_triangle(n):
    """
    returns a lists of integers
    representing the Pascal’s triangle
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            for j in range(i):
                row.append(sum(triangle[-1][j:j+2]))
        triangle.append(row)
    return triangle
