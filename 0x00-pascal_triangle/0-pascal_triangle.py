#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle
    """
    if n <= 0:
        return []

    x = []
    for i in range(n):
        y = [1]
        if x:
            for j in range(i):
                y.append(sum(x[-1][j:j+2]))
        x.append(y)
    return x
