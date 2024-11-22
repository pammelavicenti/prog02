import random
def extraimat(m,l,c,q_linha,q_coluna):
    matriz_sub=[]
    matriz_recorte=[]
    for i in range(l,q_linha+l):
        linha=[]
        for j in range(c,q_coluna+c):
            linha.append(m[i][j])
        matriz_recorte.append(linha)
    return matriz_recorte

def geramatriz(linha,coluna,minimo,maximo):
    li_matriz=[]
    valores=int()
    
    for i in range(linha):
        col_matriz=[]
        for j in range(coluna):
            col_matriz.append(random.randint(minimo,maximo))
        li_matriz.append(col_matriz)

    for x in li_matriz:
        print()
        for elemento in x:
            print("%5d" % elemento,end='')
    return li_matriz