# Exercicio de matriz
# Criar uma matriz, após criar uma matriz, criar uma sub matriz.

import random

def gerarmatriz(num_linha, num_coluna, valor_minimo, valor_maximo):
    matriz = [] 
    for i in range(num_linha):
        linha = [random.randint(valor_minimo, valor_maximo) for j in range(num_coluna)]
        matriz.append(linha)
    return matriz

def imprimir_matriz(matrizes):
    for idx, matriz in enumerate(matrizes):
        print(f"Matriz {idx + 1}:")
        for linha in matriz:
            for elemento in linha:
                print(f"{elemento:4}", end="")  # imprime cada elemento formatado
            print()  # pula para a próxima linha
        print()  # pula uma linha entre as matrizes

def criar_submatriz(matriz, lin_ini, lin_fim, col_ini, col_fim):
    submatriz = []
    for i in range(lin_ini, lin_fim + 1):
        linha = matriz[i][col_ini:col_fim + 1]
        submatriz.append(linha)
    return submatriz

def main():
    num_linha = int(input("Digite o número de linhas: "))
    num_coluna = int(input("Digite o número de colunas: "))
    valor_minimo = int(input("Digite o valor mínimo: "))
    valor_maximo = int(input("Digite o valor máximo: ")) 

    matriz = gerarmatriz(num_linha, num_coluna, valor_minimo, valor_maximo)
    
    # Imprimir a matriz completa
    print("Matriz completa:")
    imprimir_matriz([matriz])

    # Definir a submatriz
    lin_ini = int(input("Digite a linha inicial da submatriz: "))
    lin_fim = int(input("Digite a linha final da submatriz: "))
    col_ini = int(input("Digite a coluna inicial da submatriz: "))
    col_fim = int(input("Digite a coluna final da submatriz: "))

    submatriz = criar_submatriz(matriz, lin_ini, lin_fim, col_ini, col_fim)

    # Imprimir a submatriz
    print("Submatriz extraída:")
    imprimir_matriz([submatriz])

main()
