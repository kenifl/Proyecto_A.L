from fractions import Fraction

def imprimirEcuacion(x = -1, y = -1):
    placeholder = "[]"
    for i in range(unknowns):
        letter = 120
        for j in range(unknowns):
            print(f"{placeholder if (i == x and j == y) else str(matrix[i][j])}{chr(letter)}", end=" ")
            letter = (letter + 1) if letter < 122 else 97
            if j < unknowns - 1:
                print("+ ", end="")
        print(f"= {placeholder if (i == x and unknowns == y) else str(matrix[i][unknowns])}")
    print()

def one(row, column):
    if matrix[row][column] != Fraction(0, 1):
        operation = matrix[row][column]
        for i in range(unknowns+1):
            matrix[row][i] /= operation
    # imprimirEcuacion()

def zeros(row, column):
    for i in range(unknowns):
        if i != row:
            operation = matrix[i][column] * Fraction(-1, 1)
            for j in range(unknowns+1):
                matrix[i][j] = matrix[i][j] + (operation * matrix[row][j])
    # imprimirEcuacion()

unknowns = int(input("Number of unknowns: "))
matrix = []
for i in range(unknowns):
    matrix.append([0] * (unknowns + 1))

for i in range(unknowns):
    for j in range(unknowns + 1):
        imprimirEcuacion(i, j)
        matrix[i][j] = Fraction(input("Enter value of the unknown: "))
print()
imprimirEcuacion()
for i in range (unknowns):
    one(i, i)
    zeros(i, i)
imprimirEcuacion()
