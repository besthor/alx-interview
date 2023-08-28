#!/usr/bin/python3
"""
Rotate_2D_Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.
    Args:
      matrix (list of lists: The input 2D matrix to be rotated
    """


  """
  Iterate through the matrix layers
  """
    for i in range(int(len(matrix) / 2)):
  """ Iterate thorugh the elements within each layer
  """
        for j in range(i, (len(matrix) - i - 1)):
  """ Calculate the positions of the elements in the rotation
  """
            x = (len(matrix) - 1 - j)
""" Store the current element
"""
            tmp = matrix[i][j]
""" Perform the rotation of elements
"""
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[(len(matrix) - i - 1)][x]
            matrix[(len(matrix) - i - 1)][x] = matrix[j][(len(matrix) - i - 1)]
            matrix[j][(len(matrix) - i - 1)] = tmp
