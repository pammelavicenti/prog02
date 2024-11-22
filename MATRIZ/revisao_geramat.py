# Crie uma matriz com numeros sortidos de 4x4 e mostre na tela.
# A seguir, crie uma submatriz.

import random


def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        l = []
        for j in range(colunas):
            valor = random.randint(1, 10)
            l.append(valor)
        matriz.append(l)
    return matriz

def extrair_submatriz(matriz, l, c, tamanho=2):
    submatriz = []
    for i in range(l, l + tamanho):
        linha = []
        for j in range(c, c + tamanho):
            linha.append(matriz[i][j])  # Extrai o valor da posição específica
        submatriz.append(linha)
    return submatriz


linhas = 4
colunas = 4

# Cria a matriz principal
minha_matriz = criar_matriz(linhas,colunas)

print("\nMinha matriz é: ")
for l in minha_matriz:
    print(l)   

# Extrair submatriz 
submatriz_extraida = extrair_submatriz(minha_matriz, 1, 1) 

print("\nSubmatriz extraida:")
for l in submatriz_extraida:
    print(l)   