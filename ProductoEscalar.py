# Producto escalar

f = int(input ("Introduzca el número de filas de sus matrices: "))
c = int(input ("Introduzca el número de columnas de sus matrices: "))

m1 = []
mres = []
for i in range (f):
	m1.append( [0] * c)
	mres.append( [0] * c)

print ("\nMatriz")
print("----------------------------\n")

for i in range(f):
		for j in range(c):
			mres[i][j] = int(input("Posición (" + str(i+1) + "," + str(j+1) + "): "))

k=float(input ("Ingrese el número por el cuál desea multiplicar: "))

for i in range(f):
	for j in range(c):
            mres[i][j] += m1[i][j]

for i in range(f):
	for j in range(c):
            mres[i][j] = mres[i][j] * k

print ("\nResultado")
print("----------------------------")
print (mres)
