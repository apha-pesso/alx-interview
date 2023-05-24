#!/usr/bin/python3
'''Island perimeter'''


def island_perimeter(grid):
    '''Calculate perimeter'''
    perimeter = 0
    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            if col == 1:
                perimeter += 4

                if row_idx > 0 and row_idx < (len(grid) - 1):
                    if grid[row_idx - 1][col_idx] == 1:
                        perimeter -= 1

                    if grid[row_idx + 1][col_idx] == 1:
                        perimeter -= 1

                    if row[col_idx + 1] == 1:
                        perimeter -= 1

                    if row[col_idx - 1] == 1:
                        perimeter -= 1

    return perimeter
