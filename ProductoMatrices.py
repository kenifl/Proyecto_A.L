from fractions import Fraction

# Producto de matrices

def checartamano(c1,f2):
    if c1 == f2:
        print("Ready for data capture\n")
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


    print("\n1st Matrix")
    print("---------------\n")
    for i in range(f1):
            for j in range(c1):
                m1[i][j] = Fraction(input("Position (" + str(i+1) + "," + str(j+1) + "): "))

    print("\n2nd Matrix")
    print("---------------\n")
    for i in range(f2):
            for j in range(c2):
                m2[i][j] = Fraction(input("Position (" + str(i+1) + "," + str(j+1) + "): "))
    print()

    
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                mres[i][j] += m1[i][k] * m2[k][j]

    for element in mres:
        print(element)


print ("\n1st Matrix")
print("----------------------------\n")
f1 = Fraction(input("Enter the number of rows in your first matrix: "))
c1= Fraction(input("Enter the number of columns in your first matrix: "))
print()

print ("\n2nd Matrix")
print("----------------------------\n")
f2 = Fraction(input ("Enter the number of rows in your second matrix: "))
c2= Fraction(input ("Enter the number of columns in your second matrix: "))
print()

v = checartamano(c1,f2)

if v == True:
    calcular()
else: 
    print()