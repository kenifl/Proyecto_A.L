#SUMA

filas = int(input ("Introduzca el número de filas de sus matrices: "))
columnas = int(input ("Introduzca el número de columnas de sus matrices: "))

matriz_1 = []
matriz_2 = []
matriz_3 = []
for i in range (filas):
	matriz_1.append( [0] * columnas)
	matriz_2.append( [0] * columnas)
	matriz_3.append( [0] * columnas)

print ("Ingrese su Matriz 1")
for i in range(filas):
		for j in range(columnas):
			matriz_1[i][j] = int(input('Elemento (%d,%d): ' % (i, j)))

print("Ingrese su Matriz 2")
for i in range(filas):
	for j in range(columnas):
			matriz_2[i][j] = int(input('Elemento (%d,%d): ' % (i, j)))
            

for i in range(filas):
	for j in range(columnas):
			matriz_3[i][j] += matriz_1[i][j] + matriz_2[i][j]
print ("Su matriz resultante es: ")
print (matriz_3)

