from fractions import Fraction
#ADDITION
rows = int(input ("Enter the number of rows: "))
columns = int(input ("Enter the number of columns: "))

matrix_1 = []
matrix_2 = []
matrix_3 = []
for i in range (rows):
	matrix_1.append( [0] * columns)
	matrix_2.append( [0] * columns)
	matrix_3.append( [0] * columns)

print ("Enter your first matrix")
for i in range(rows):
		for j in range(columns):
			matrix_1[i][j] = Fraction(input('Element (%d,%d): ' % (i, j)))

print("Enter your second matrix")
for i in range(rows):
	for j in range(columns):
			matrix_2[i][j] = Fraction(input('Element (%d,%d): ' % (i, j)))
            

for i in range(rows):
	for j in range(columns):
			matrix_3[i][j] += matrix_1[i][j] + matrix_2[i][j]
print ("Resulting matrix: ")
print (matrix_3)

