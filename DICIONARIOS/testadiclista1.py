# Exercicio 01 da lista 01 de dicionários

import dicionarios_lista01 as lib

def main():
    dic = {'c1': 'vermelho', 'c2': 'verde', 'c3': None}

    print(dic)
    dic = lib.eliminaNones(dic)
    print(dic)
# fim main
main()