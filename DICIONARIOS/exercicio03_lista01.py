'''
Escreva   um   programa   Python   que   converta   listas   de   entrada   em   uma   lista   de
dicionários aninhados. O exemplo a seguir ilustra o problema para 3 listas de entrada.
Exemplo:
Listas de entrada
['S001', 'S002', 'S003', 'S004']
['Pedra da Cebola', 'Praça do Papa', 'Costa Pereira', 'Reserva Paulo Vinhas']
[85, 98, 89, 92]
Dicionário aninhado de saída
[{'S001': {'Pedra da Cebola': 85}}, {'S002': {'Praça do Papa': 98}}, {'S003': {'Costa Pereira':
89}}, {'S004': {'Reserva Paulo Vinhas': 92}}]
Desafio:   consegue-se   construir   um   código   para   uma   quantidade   de   listas   de   entrada
qualquer???

'''

def converter_para_dicionarios_aninhados(lista1, lista2, lista3):
    """
    Função que converte três listas em uma lista de dicionários aninhados.
    Cada elemento das listas é combinado para formar um dicionário no formato:
    {chave: {sub_chave: valor}}
    """
    resultado = []  # Inicializa uma lista vazia para armazenar os dicionários resultantes.
    
    for i in range(len(lista1)):  # Itera pelos índices das listas, assumindo que todas têm o mesmo tamanho.
        # Cria um dicionário no formato {chave: {sub_chave: valor}}
        dicionario = {lista1[i]: {lista2[i]: lista3[i]}}
        resultado.append(dicionario)  # Adiciona o dicionário criado à lista resultado.
    
    return resultado  # Retorna a lista contendo os dicionários aninhados.

# Listas de entrada
ids = ['S001', 'S002', 'S003', 'S004']  # Lista com os identificadores (chaves principais).
locais = ['Pedra da Cebola', 'Praça do Papa', 'Costa Pereira', 'Reserva Paulo Vinhas']  # Lista com os nomes dos locais (subchaves).
pontuacoes = [80, 90, 75, 85]  # Lista com as pontuações (valores).

# Chama a função para converter as listas em uma lista de dicionários aninhados
resultado = converter_para_dicionarios_aninhados(ids, locais, pontuacoes)

# Exibe o resultado final no console
print(resultado)
