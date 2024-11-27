# Lista 2, exercicio 7
def loadAgenda(filename):
    d = {}
    arq = open(filename, "rt")

    linha = arq.readline()
    while linha != "":
        lst = linha.strip().split(", ")
        d[lst[0]] = {"nome": lst [1], "email": lst [2]}
        linha = arq.readline()


    arq.close()
    return d 
# fim loadAgenda

def main():
    agenda = loadAgenda("bdagendatelefonica.txt")
    tel = input("Entre com o telefone: ")
    if tel in agenda:
        print("telefone: ", tel)
        print("Nome: ", agenda[tel]["nome"])
        print("Nome: ", agenda[tel]["email"])
        print()
    else:
        print("Número de telefone não encontrado!\n")
    tel = input("Entre com o telefone: ")

main()
