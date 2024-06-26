#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an Island

    Args:
        grid (array): the given array
    Return:
        The perimeter of the Island described in the grid
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
