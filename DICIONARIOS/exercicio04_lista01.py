"""Escreva   um   programa   Python   que   filtre/extraia   altura   e   
peso   dos   estudantes armazenados em um dicionário de entrada.
Exemplo:
Dicionário de entrada
{'César': (1.77, 72), 'Aldo': (1.67, 65), 'Maria': (1.65, 68), 'Pedro': (1.72, 66)}
Dicionário de saída: conteúdos altura > 1.75 e peso > 70.
{'César': (1.77,72)}"""

def main():

    dicionario = {'César': (1.77, 72), 'Aldo': (1.67, 65), 'Maria': (1.65, 68), 'Pedro': (1.72, 66)}


    for nome, valor in dicionario.items():
        altura, peso = valor

        if altura > 1.75 and peso > 70:
            print(f"{nome} atende os critérios: Altura = {altura} m, Peso = {peso} kg")
main()