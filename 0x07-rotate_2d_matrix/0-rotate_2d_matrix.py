#!/usr/bin/python3
"""
a python module to rotate a matrix by 90 degree
"""


def rotate_2d_matrix(matrix):
    """
    rotate_2d_matrix - function to rotate a matrix by 90 clockwise
    Arguments:
        matrix: the given matrix
    Returns:
        nothing
    """
    """Transpose a matrix"""
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    """reverse the matrix by column, 1st col becomes last col
    let l to start from first column and increment to end
    let r to start from last column and decrement to first
    """
    for n in range(len(matrix)):
        r = len(matrix[n]) - 1
        lft = 0
        while lft < r:
            tmp = matrix[n][lft]
            matrix[n][lft] = matrix[n][r]
            matrix[n][r] = tmp
            lft += 1
            r -= 1
