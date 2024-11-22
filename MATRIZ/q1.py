# PRIMEIRA QUESTÃO DA PROVA DE PROGRAMAÇÃO 2

def loadMat(fileName):
    matriz = []
    with open(fileName, "r") as arquivo:
        for linha in arquivo:
            # Converte cada elemento de cada linha para um número inteiro e adiciona à matriz
            linha_convertida = []
            for elemento in linha.strip().split():  # Divide a linha em elementos e remove espaços extras
                linha_convertida.append(int(elemento))  # Converte cada elemento para inteiro e adiciona à lista
            matriz.append(linha_convertida)
    return matriz

def ts(mat):
    # Cria uma matriz triangular superior com zeros nas posições inferiores
    triangular_sup = []
    for i in range(len(mat)):
        linha = []
        for j in range(len(mat[i])):
            if j >= i:
                linha.append(mat[i][j])
            else:
                linha.append(0)
        triangular_sup.append(linha)
    return triangular_sup

def ti(mat):
    # Cria uma matriz triangular inferior com zeros nas posições superiores
    triangular_inf = []
    for i in range(len(mat)):
        linha = []
        for j in range(len(mat[i])):
            if j <= i:
                linha.append(mat[i][j])
            else:
                linha.append(0)
        triangular_inf.append(linha)
    return triangular_inf

def printMat(mat):
    for linha in mat:
        print(" ".join(str(elemento) for elemento in linha))

def main():
    # Carrega a matriz a partir do arquivo
    matriz = loadMat("C:\\Users\\Pammela\\OneDrive\\Área de Trabalho\\PYTHON\\PROG2\\MATRIZ\\q1mat.txt")

    print("Matriz Original:")
    printMat(matriz)

    print("\nMatriz Triangular Superior:")
    triangular_sup = ts(matriz)
    printMat(triangular_sup)

    print("\nMatriz Triangular Inferior:")
    triangular_inf = ti(matriz)
    printMat(triangular_inf)

# Executa o programa principal
if __name__ == "__main__":
    main()
