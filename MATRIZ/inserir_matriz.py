from print_Mat import printMat


def insere(M, l, c, m):
    linhasM = len(M)
    colsM = len(M[0])
    linhas_m = len(m)
    cols_m = len(m[0])

    r = 0
    
    for i in range(l, l + linhas_m):
        s = 0
        for j in range(c, c + cols_m):
            M[i][j] = m[r][s]
            s = s + 1
        r = r + 1
    return M
#fim extrai matriz

def main():
    MM = [[5,4,1,8,3,6],[3,0,5,6,7,4],[9,1,2,8,4,3],[4,5,1,9,0,2],[9,0,7,4,1,3]]
    mm = [[1,1,1],[1,1,1],[1,1,1]]

    printMat(MM)
    print()
    printMat(mm)
    print()
    MM = insere(MM,1,2,mm)
    printMat(MM)
    print()
# fim main

main()