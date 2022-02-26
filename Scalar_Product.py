# Scalar Product

from fractions import Fraction

k = float(input("Enter the number you wish to multiply by: "))

print ("\nMatrix")
print("----------------------------\n")

f = int(input("Enter the number of rows in your matrix: "))
c = int(input("Enter the number of columns in your matrix: "))

print()

m1 = []
mres = []

for i in range (f):
	m1.append( [0] * c)
	mres.append( [0] * c)

for i in range(f):
		for j in range(c):
			mres[i][j] = Fraction(input("Position (" + str(i+1) + "," + str(j+1) + "): "))

for i in range(f):
	for j in range(c):
            mres[i][j] *= k

print ("\nResult")
print("----------------------------")
print (mres)
