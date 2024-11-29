def main():

    arquivo = open("bdmegasena.txt","rt")
    linha = arquivo.readline()
    dicionario = {}

    while linha !="":
        descarte = linha.strip().split("\t") # Criando uma lista com os dados
        for i in descarte:
            
            if i in dicionario:
                dicionario[i] += 1
            else:
                dicionario[i] = 1
        linha = arquivo.readline()       

    print(dicionario)

    arquivo.close()

if __name__=="__main__":
    main()