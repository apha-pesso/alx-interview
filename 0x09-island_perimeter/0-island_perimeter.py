#!/usr/bin/python3
'''Island perimeter'''


def island_perimeter(grid):
    '''Island perimeter'''
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i > 0 and i < (len(grid) - 1):
                    if grid[i - 1][j] == 0:
                        perimeter += 1

                    if grid[i + 1][j] == 0:
                        perimeter += 1

                    if grid[i][j - 1] == 0:
                        perimeter += 1

                    if grid[i][j + 1] == 0:
                        perimeter += 1
                else:
                    return 0
    return perimeter
