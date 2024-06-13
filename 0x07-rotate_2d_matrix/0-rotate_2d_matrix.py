#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix) -> None:
    """
    Rotate it 90 degrees clockwise

    Args:
        matrix: the matrix to rotate
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
