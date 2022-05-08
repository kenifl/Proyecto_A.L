# Matrix Product

def calculate(m1 , m2):
   # print("Filas 1:",len(m1),"Columnas 1:",len(m1[0]))
   # print("Filas 2:",len(m2),"Columnas 2:",len(m2[0]))
    mres=[]
    row = []
    valor = 0
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                #print(i,j,k)
                valor += m1[i][k] * m2[k][j]
            row.append(valor)
            valor = 0
        mres.append(row)
        row = []

    return mres
