'''
Escreva um programa Python para criar um dicionário agrupando uma sequência de
pares chaves-valor vindos de listas.
Exemplo:
Listas de entrada:
[('amarelo', 1), ('azul', 2), ('amarelo', 3), ('azul', 4), ('vermelho', 1)]
Dicionário de saída:
{'amarelo': [1, 3], 'azul': [2, 4], 'vermelho': [1]}

'''
def agrupar_pares(lista):
    """
    Agrupa os valores associados a cada chave em uma lista.
    
    :param lista: Lista de pares (chave, valor)
    :return: Dicionário agrupado por chave
    """
    dicionario_agrupado = {}  # Dicionário vazio para armazenar os grupos
    
    for chave, valor in lista:  # Itera sobre cada par (chave, valor) na lista
        if chave not in dicionario_agrupado:  # Se a chave ainda não está no dicionário
            dicionario_agrupado[chave] = []  # Inicializa uma lista vazia para a chave
        dicionario_agrupado[chave].append(valor)  # Adiciona o valor à lista correspondente à chave
    
    return dicionario_agrupado

# Listas de entrada
pares = [('amarelo', 1), ('azul', 2), ('amarelo', 3), ('azul', 4), ('vermelho', 1)]

# Agrupar os pares na lista
resultado = agrupar_pares(pares)

# Exibir o resultado
print(resultado)
