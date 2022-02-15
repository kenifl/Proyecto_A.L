from hashlib import new
from numpy import matrix


def transpose(matrix):
    """
    Transpose a matrix.
    """
    new_matrix = []
    #return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        new_matrix.append(row)
    return new_matrix
def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        for i in range(len(matrix)):
            determinant_number += matrix[0][i] * (-1)**(i+1) * determinant()
            print(determinant_number)
    return determinant_number
matrix = [[-1, 2, 4], [6, 3, 5], [-3, 7, 0]]
print(determinant(matrix))