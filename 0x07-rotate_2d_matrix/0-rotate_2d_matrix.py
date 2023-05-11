#!/usr/bin/python3
'''Rotate a matrix'''


def rotate_2d_matrix(matrix):
    '''Rotate 2d matrix'''
    mat_len = len(matrix)

    # Transpose matrix
    for i in range(mat_len):
        for j in range(i, mat_len):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each of the rows
    for i in range(mat_len):
        matrix[i] = matrix[i][::-1]
