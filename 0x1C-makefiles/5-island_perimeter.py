#!/usr/bin/python3
""" function def island_perimeter(grid) """


def island_perimeter(grid):
    """ returns the perimeter of the island described in grid """
    pmeter = 0

    nrows = len(grid)

    if grid != []:
        ncolumns = len(grid[0])

    for a in range(nrows):
        for b in range(ncolumns):
            if grid[a][b] == 1:
                if (a - 1) == -1 or grid[a - 1][b] == 0:
                    pmeter += 1
                if (a + 1) == nrows or grid[a + 1][b] == 0:
                    pmeter += 1
                if (b - 1) == -1 or grid[a][b - 1] == 0:
                    pmeter += 1
                if (b + 1) == ncoloumns or grid[a][b + 1] == 0:
                    pmeter +=1

    return pmeter
