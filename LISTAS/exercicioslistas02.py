# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

def inverter_vetor():

# Criando um vetor vazio
    vetor = []

# Lendo 10 numeros e adicionando ao vetor 
    for i in range(10):
        numero = float(input("Digite o numero {}: ".format(i+1)))
        vetor.append(numero)

# Invertendo a ordem do vetor
    vetor.reverse()

# Mostrando os números do vetor 
    print("Os numeros na ordem inversa são:")
    for numero in vetor:
        print(numero)

# Chamando a função para executar o programa
inverter_vetor()
