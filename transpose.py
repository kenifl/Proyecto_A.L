import numpy as np

def transpose(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        new_matrix.append(row)
    return new_matrix
def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0,0]
    else:
        determinant_number = 0
        for i in range(len(matrix)):
            determinant_number += matrix[0,i] * (-1)**(i+1) * determinant(slice_matrix(matrix,i))
    return determinant_number
def slice_matrix(matrix,i):
    new_matrix=[]
    for j in range(len(matrix)):
        if j!=i:
            new_matrix.append(matrix[1:,j])
    return np.array(new_matrix)
matrix = [[-10, 5, -3], [2, -2, 2], [17, -5, 1]]
new_matrix = np.array(matrix)
print(determinant(new_matrix))
