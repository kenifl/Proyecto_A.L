def suma_matriz(matrix_1, matrix_2):
	rows = len(matrix_1)
	columns = len(matrix_1[0])
	matrix_3 = []
	for i in range(rows):
		matrix_3.append([0] * columns)
	for i in range(rows):
		for j in range(columns):
			matrix_3[i][j] += matrix_1[i][j] + matrix_2[i][j]
	return matrix_3
