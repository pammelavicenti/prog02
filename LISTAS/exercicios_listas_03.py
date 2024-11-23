# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

def calcular_media():

# Criar uma lista vazia para armazenar as notas
    notas = []

# Ler as 4 notas e adicioná-las à lista 
    for i in range(4):
        nota = float(input(f"Digite a {i+1} nota: "))
        notas.append(nota)

# Calcular a média
    media = sum(notas) / len(notas)

# Exibir as notas e a media
    print("As notas são:", notas)
    print(f" A media das notas é: {media: .2f}")
  
# Chamando a função para executar o programa
calcular_media()