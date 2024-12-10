'''Crie um dicionário que contenha palavras em inglês como chaves e suas traduções em português
como valores. Escreva uma função que, dado uma palavra em inglês, retorne sua tradução. Caso
a palavra não exista no dicionário, exiba uma mensagem informando que a tradução não está
disponível'''

dic = {
    "apple": "maçã",
    "book": "livro",
    "computer": "computador",
    "dog": "cachorro",
    "friend": "amigo",
    "house": "casa",
    "love": "amor",
    "mountain": "montanha",
    "night": "noite",
    "rain": "chuva",
    "school": "escola",
    "tree": "árvore",
    "water": "água",
    "work": "trabalho",
    "city": "cidade",
    "music": "música",
    "car": "carro",
    "family": "família",
    "sun": "sol",
    "food": "comida"
}
    
def escreva_palavra(palavra):
    traducao = dic.get(palavra.lower())  # Busca a palavra no dicionário, ignorando maiúsculas/minúsculas
    if traducao:
        return (f"A tradução de '{palavra}' é '{traducao}'.")
    else:
        return (f"A tradução de '{palavra}' não está disponível.")
    
print(dic)
palavra = input("Escreva uma palavra em inglês: ")
print(escreva_palavra(palavra))





