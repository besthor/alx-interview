#!/usr/bin/python3
"""
A function def island_perimeter(grid) 
that returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """Functions outputs the peremeter of the Island"""
    perimeter = 0
    grid_lenght = len(grid)
    for row in range(grid_lenght):
        for column in range(len(grid[row])):
            if grid[row][column] == 1:
                if row - 1 < 0 or grid[row - 1][column] == 0:
                    perimeter += 1
                if column - 1 < 0 or grid[row][column - 1] == 0:
                    perimeter += 1
                if column + 1 >= len(grid[row]) or grid[row][column + 1] == 0:
                    perimeter += 1
                if row + 1 >= grid_lenght or grid[row + 1][column] == 0:
                    perimeter += 1
    return perimeter
