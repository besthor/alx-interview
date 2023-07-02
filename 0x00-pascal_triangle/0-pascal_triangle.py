#!/usr/bin/python3
"""
create a function def pascal_triangle(n)
Returns a list of list of integers
representing the Pascal's triangle of (n)
Returns an empty list if n <= 0
you can assume n will always be an integer
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            if j < i:
                if j == 0:
                    triangle[i].append(1)
                else:
                    triangle[i].append(triangle[i - 1][j] + triangle[i - 1][j - 1])
            elif j == i:
                triangle[i].append(1)

    return triangle

