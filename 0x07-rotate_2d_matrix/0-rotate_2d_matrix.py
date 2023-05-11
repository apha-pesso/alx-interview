#!/usr/bin/python3
'''Rotate a matrix'''


def rotate_2d_matrix(matrix):
    '''Rotate 2d matrix'''
    l = len(matrix)

    # Transpose matrix
    for i in range(l):
        for j in range(i, l):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each of the rows
    for i in range(l):
        matrix[i] = matrix[i][::-1]

