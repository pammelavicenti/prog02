# Exercicio 09 da lista 01 de dicionários

def valsFromAKey(lstdics, chave):
    lstout = []
    for d in lstdics:
        lstout.append(d[chave])
    return lstout
# Fim valsFromAKey

def main():
    L = [{'Matemática': 90, 'Ciência': 92}, {'Matemática': 89, 'Ciência': 94}, {'Matemática': 92, 'Ciência': 88}]
    arq = open("valoresFromAKey.txt", "wt")

    outA = valsFromAKey(L,"Ciência")
    outB = valsFromAKey(L, "Matemática")

    print(L)
    print(outA)
    print(outB)

    for i in range(len(outA)):
        if i < len(outA) -1:
            arq.write(f"{outA[i]},")  # Adiciona vírgula entre os valores
        else:
            arq.write(f"{outA[i]}")  # Não adiciona vírgula no último valor

    arq.close()  # Fecha o arquivo

main()