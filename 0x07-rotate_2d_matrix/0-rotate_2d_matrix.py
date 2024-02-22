#!/usr/bin/python3
""" 2D Matrix rotation """


def rotate_2d_matrix(matrix):
    """ Rotates 2D matrix 90 decreaseo """
    matrix.reverse()
    m_len = len(matrix)
    for i in range(m_len):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
