# Matrix Product

def calculate(m1 , m2):
    mres=[]
    row = []
    valor = 0
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                valor += m1[i][k] * m2[k][j]
            row.append(valor)
            valor = 0
        mres.append(row)
        row = []

    return mres
