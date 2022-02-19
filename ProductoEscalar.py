# Producto escalar
k=float(input("Ingrese el número por el cuál desea multiplicar: "))

print ("\nMatriz")
print("----------------------------\n")
f = int(input ("Introduzca el número de filas de su matriz: "))
c = int(input ("Introduzca el número de columnas de su matriz: "))
print()

m1 = []
mres = []
for i in range (f):
	m1.append( [0] * c)
	mres.append( [0] * c)

for i in range(f):
		for j in range(c):
			mres[i][j] = float(input("Posición (" + str(i+1) + "," + str(j+1) + "): "))

for i in range(f):
	for j in range(c):
            mres[i][j] *= k

print ("\nResultado")
print("----------------------------")
print (mres)
