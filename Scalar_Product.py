# Scalar Product

from fractions import Fraction

def scalar_product(matrix, escalar):
	mres = []
	for i in range(len(matrix)):
		mres.append([])
		for j in range(len(matrix[i])):
			mres[i].append(matrix[i][j] * escalar)
	return mres

