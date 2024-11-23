# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os:

def ler_e_mostrar_vetor():

# Criando um vetor vazio
    vetor = []

# Lendo 5 numeros e adicionando ao vetor 
    for i in range(5):
        numero = int(input("Digite o numero {}: ".format(i+1)))
        vetor.append(numero)

# Mostrando os números do vetor 
    print("Os numeros digitados foram:")
    for numero in vetor:
        print(numero)

# Chamando a função para executar o programa
ler_e_mostrar_vetor()
