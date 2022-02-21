from fractions import Fraction

# Producto escalar

k = Fraction(input("Enter the number you wish to multiply by: "))

print ("\nMatriz")
print("----------------------------\n")

f = Fraction(input("Enter the number of rows in your matrix: "))
c = Fraction(input("Enter the number of columns in your matrix: "))

print()

m1 = []
mres = []

for i in range (f):
	m1.append( [0] * c)
	mres.append( [0] * c)

for i in range(f):
		for j in range(c):
			mres[i][j] = Fraction(input("Posición (" + str(i+1) + "," + str(j+1) + "): "))

for i in range(f):
	for j in range(c):
            mres[i][j] *= k

print ("\nResultado")
print("----------------------------")
print (mres)
