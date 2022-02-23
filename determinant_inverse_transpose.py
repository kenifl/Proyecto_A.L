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

def slice_matrix_2D(matrix,i,j):
    pos_r = 0
    pos_c = 0
    new_matrix = np.empty((matrix.shape[0]-1,matrix.shape[1]-1))
    for k in range(matrix.shape[0]):
        for m in range(matrix.shape[1]):
            if k!=i and m!=j:
                new_matrix[pos_r,pos_c] = matrix[k,m]
                if pos_c < new_matrix.shape[1]-1:
                    pos_c += 1
                else:
                    pos_c = 0
                    pos_r += 1
    return new_matrix

def adjugate(matrix):
    adjugate_matrix=np.copy(matrix)
    for i in range(adjugate_matrix.shape[0]):
        for j in range(adjugate_matrix.shape[1]):
            adjugate_matrix[i,j] = determinant(slice_matrix_2D(matrix,i,j))*(-1)**(i+j+3)
    adjugate_matrix = transpose(adjugate_matrix)
    return adjugate_matrix

    
def inverse(matrix):
    inverse_matrix = adjugate(matrix)/determinant(matrix)
    return inverse_matrix
