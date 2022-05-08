from fractions import Fraction

def one(row, column, matrix, unknowns):
    if matrix[row][column] != Fraction(0, 1):
        operation = matrix[row][column]
        print(f"R{row+1}/{operation}")
        for i in range(unknowns+1):
            matrix[row][i] /= operation
    return matrix

def zeros(row, column, matrix, unknowns):
    for i in range(unknowns):
        if i != row:
            print(matrix[i][column])
            operation = matrix[i][column] * Fraction(-1, 1)
            print(f"{operation}R{row} + R{i}")
            for j in range(unknowns+1):
                matrix[i][j] = matrix[i][j] + (operation * matrix[row][j])
    return matrix

def gaussJordan(matrix):
    unknowns = 0
    if len(matrix) < len(matrix[0])-1:
        unknowns = len(matrix)
    else:
        unknowns = len(matrix[0])-1
    temp = matrix.copy()
    for i in range(unknowns):
        temp = one(i, i, temp, unknowns)
        temp = zeros(i, i, temp, unknowns)
    return matrix
