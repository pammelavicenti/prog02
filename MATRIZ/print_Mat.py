def printMat(mat):
    linha = len(mat)
    coluna = len(mat[0])

    for i in range (linha):
        for j in range (coluna):
            print('%5d' % mat[i][j], end='')
        print()