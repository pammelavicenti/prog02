def loadMatriz(nome_arquivo):
    matriz = []
    with open(nome_arquivo, "r") as arquivo: # indica ao Python que queremos abrir o arquivo no modo de leitura.
        for linha in arquivo:
                # Converte cada elemento de cada linha para um número inteiro e adiciona à matriz
            linha_convertida = list(map(int, linha.strip().split()))
            matriz.append(linha_convertida)
    return matriz

# Chama a função e armazena o resultado em uma variável
minha_matriz = loadMatriz("C:/Users/Pammela/OneDrive/Área de Trabalho/PYTHON/PROG2/MATRIZ/matriz.txt")

# Imprime a matriz carregada
print("Matriz carregada:")
for linha in minha_matriz:
    print(linha)


def salvaMatriz(mat, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo: #"w" (write): Abre o arquivo em modo de escrita. Esse modo sobrescreve o conteúdo existente ou cria um novo arquivo se ele não existir.
        for linha in mat:
            linha_formatada = ""
            for num in linha:
                linha_formatada += str(num) + " "
            linha_formatada = linha_formatada.strip()  # Remove o espaço extra no final
            
            # Escreve a linha formatada no arquivo
            arquivo.write(linha_formatada + "\n")  # Adiciona uma nova linha após cada linha da matriz

# Salva a matriz carregada no arquivo especificado
salvaMatriz(minha_matriz, "C:/Users/Pammela/OneDrive/Área de Trabalho/PYTHON/PROG2/MATRIZ/matriz_salva.txt")
