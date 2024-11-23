"""Faça um Programa que leia um vetor de 10 caracteres, 
e diga quantas consoantes foram lidas. Imprima as consoantes."""

def contar_consoantes():

# Criando um vetor vazio para armazenar os caracteres 
    caracteres = []

# Ler os 10 caracteres e adicioná-los ao vetor

    for i in range(10):
        caracter = input(f"Digite o {i+1} caractere: ")
        caracteres.append(caracter)

# Definindo as vogais
    vogais = 'aeiouAEIOU'

# Inicializando o contador de consoantes 
    cont_consoantes = 0

# Iterando sobre os caracteres e contando as consoantes 
    print("As consoantes são: ")
    for caracter in caracteres:
        if caracter not in vogais and (caracter >= 'a' and caracter <= 'z' or caracter >= 'A' and caracter <= 'Z'):
            print(caracter)
            cont_consoantes += 1

# Imprimindo o numero total de consoantes 
    print(f"Foram encontradas {cont_consoantes} consoantes.")
  
# Chamando a função para executar o programa
contar_consoantes()

