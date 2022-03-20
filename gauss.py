from fractions import Fraction


unknowns = int(input("Number of unknowns: "))
res = [0] * unknowns
matrix = []
for i in range(unknowns):
    matrix.append([0] * (unknowns + 1))


def imprimirEcuacion(x=-1, y=-1):
    placeholder = "[]"
    for i in range(unknowns):
        letter = 120
        for j in range(unknowns):
            print(
                f"{placeholder if (i == x and j == y) else str(matrix[i][j])}{chr(letter)}", end=" ")
            letter = (letter + 1) if letter < 122 else 97
            if j < unknowns - 1:
                print(" ", end="")
        print(
            f"| {placeholder if (i == x and unknowns == y) else str(matrix[i][unknowns])}")
    print()


def one(row, column):
    operation = matrix[row][column]
    print(f"{1 / operation}R{row}")
    if matrix[row][column] != Fraction(0, 1):
        for i in range(unknowns+1):
            matrix[row][i] /= operation
    imprimirEcuacion()


def zeros(row, column):
    for i in range(row+1 , unknowns):
        operation = matrix[i][column] * Fraction(-1, 1)
        print(f"{operation}R{row} + R{i}")
        for j in range(unknowns+1):
            matrix[i][j] = matrix[i][j] + (operation * matrix[row][j])
    imprimirEcuacion()

def resultado():
    for i in reversed(range(unknowns)):
        res[i] = matrix[i][unknowns]
        for j in range(unknowns):
            if j != i:
                res[i] -= matrix[i][j] * res[j]
    print(res)

for i in range(unknowns):
    for j in range(unknowns + 1):
        imprimirEcuacion(i, j)
        matrix[i][j] = Fraction(input("Enter the value of the unknown: "))
print()
imprimirEcuacion()
for i in range(unknowns):
    one(i, i)
    zeros(i, i)
imprimirEcuacion()
resultado()
