from fractions import Fraction

def imprimirEcuacion(x = -1, y = -1):
    placeholder = "[]"
    for i in range(unknowns):
        letter = 120
        for j in range(unknowns):
            print(f"{placeholder if (i == x and j == y) else str(matrix[i][j])}", end=" ")
            letter = (letter + 1) if letter < 122 else 97
            if j < unknowns - 1:
                print(" ", end="")
        print(f"= {placeholder if (i == x and unknowns == y) else str(matrix[i][unknowns])}")
    print()
# def imprimirEcuacion(x = -1, y = -1):
#     placeholder = "[]"
#     for i in range(unknowns):
#         letter = 120
#         for j in range(unknowns):
#             print(f"{placeholder if (i == x and j == y) else str(matrix[i][j])}{chr(letter)}", end=" ")
#             letter = (letter + 1) if letter < 122 else 97
#             if j < unknowns - 1:
#                 print("+ ", end="")
#         print(f"= {placeholder if (i == x and unknowns == y) else str(matrix[i][unknowns])}")
#     print()

def one(row, column):
    if matrix[row][column] != Fraction(0, 1):
        operation = matrix[row][column]
        print(f"R{row+1}/{operation}")
        for i in range(unknowns+1):
            matrix[row][i] /= operation
    imprimirEcuacion()

def zeros(row, column):
    for i in range(unknowns):
        if i != row:
            operation = matrix[i][column] * Fraction(-1, 1)
            print(f"{operation}R{row} + R{i}")
            for j in range(unknowns+1):
                matrix[i][j] = matrix[i][j] + (operation * matrix[row][j])
    imprimirEcuacion()

unknowns = int(input("Number of unknowns: "))
matrix = []
for i in range(unknowns):
    matrix.append([0] * (unknowns + 1))

for i in range(unknowns):
    for j in range(unknowns + 1):
        imprimirEcuacion(i, j)
        matrix[i][j] = Fraction(input("Enter value of the unknown: "))
#matrix = [[1, 2, 1, 1, 2], [2, 4, 3, 4, 7], [-1, -2, 2, 5, 3], [3, 6, 2, 1, 3], [4, 8, 6, 8, 9]]
#unknowns = 5
#matrix = [[Fraction(1, 1), Fraction(2, 1), Fraction(1, 1), Fraction(1, 1), Fraction(2, 1), Fraction(0, 1)], [Fraction(2, 1), Fraction(4, 1), Fraction(3, 1), Fraction(4, 1), Fraction(7, 1), Fraction(0, 1)], [Fraction(-1, 1), Fraction(-2, 1), Fraction(2, 1), Fraction(5, 1), Fraction(3, 1), Fraction(0, 1)], [Fraction(3, 1), Fraction(6, 1), Fraction(2, 1), Fraction(1, 1), Fraction(3, 1), Fraction(0, 1)], [Fraction(4, 1), Fraction(8, 1), Fraction(6, 1), Fraction(8, 1), Fraction(9, 1), Fraction(0, 1)]]
print()
print(matrix)
print()
imprimirEcuacion()
for i in range (unknowns):
    one(i, i)
    zeros(i, i)
imprimirEcuacion()
