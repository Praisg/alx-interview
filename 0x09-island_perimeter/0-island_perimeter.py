#!/usr/bin/python3
"""Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculate perimeter of the island described in grid
    Args:
        grid: 2d list of int containing 0 (Water) or 1 (Land)
    Return:
        the perimeter of the island
    """

    p = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    p += 1
                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    p += 1
                if (j <= 0 or grid[i][j - 1] == 0):
                    p += 1
                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    p += 1
    return p