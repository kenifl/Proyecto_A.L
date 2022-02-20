# Producto de matrices

def checartamano(c1,f2):
    if c1 == f2:
        print("Listo para capturar datos\n")
        return True
    else:
        print("Dimension Error")
        return False


def calcular():
    m1=[]
    m2=[]
    mres=[]

    for i in range(f1):
        m1.append([0] * c1)

    for i in range(f2):
        m2.append([0] * c2)

    for i in range(f1):
        mres.append([0] * c2)


    print("\nMatriz 1")
    print("---------------\n")
    for i in range(f1):
            for j in range(c1):
                m1[i][j] = float(input("Posición (" + str(i+1) + "," + str(j+1) + "): "))

    print("\nMatriz 2")
    print("---------------\n")
    for i in range(f2):
            for j in range(c2):
                m2[i][j] = float(input("Posición (" + str(i+1) + "," + str(j+1) + "): "))
    print()

    
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                mres[i][j] += m1[i][k] * m2[k][j]

    for element in mres:
        print(element)


print ("\nMatriz 1")
print("----------------------------\n")
f1 = int(input ("Introduzca el número de filas de su matriz 1: "))
c1= int(input ("Introduzca el número de columnas de su matriz 1: "))
print()

print ("\nMatriz 2")
print("----------------------------\n")
f2 = int(input ("Introduzca el número de filas de su matriz 2: "))
c2= int(input ("Introduzca el número de columnas de su matriz 2: "))
print()

v = checartamano(c1,f2)

if v == True:
    calcular()
else: 
    print()
