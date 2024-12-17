'''Construa o TAD equação do segundo grau. Faça uma escolha 
para a implementação e construa a seguinte interface:

a) new_eq(ca, cb, cc)
b) getA(tad), getB(tad), getC(tad)
c) quant_raizes(tad)
d) getRaiz1(tad)
e) getRaiz2(tad)

Pesquise 3 usos de uma equação do segundo grau e construa uma
aplicação exemplo para cada um desses casos de uso.

Principal ideia do tad é a abstração e o reuso.


'''
# Função para criar a equação do segundo grau
def new_eq(ca, cb, cc):
    return {'a': ca, 'b': cb, 'c': cc, 'raiz1': None, 'raiz2': None}

# Função para obter o coeficiente A
def getA(tad):
    return tad['a']

# Função para obter o coeficiente B
def getB(tad):
    return tad['b']

# Função para obter o coeficiente C
def getC(tad):
    return tad['c']

# Função para calcular o número de raízes
def quant_raizes(tad):
    a = tad['a']
    b = tad['b']
    c = tad['c']
    
    # Calculando o discriminante (delta)
    delta = b**2 - 4*a*c
    
    if delta < 0:
        return 0  # Nenhuma raiz real
    elif delta == 0:
        return 1  # Uma raiz real (raiz dupla)
    else:
        return 2  # Duas raízes reais

# Função para calcular as raízes (quando possível)
def calcular_raizes(tad):
    a = tad['a']
    b = tad['b']
    c = tad['c']
    
    delta = b**2 - 4*a*c  # Calculando o discriminante
    
    if delta >= 0:  # Se houver raízes reais
        raiz1 = (-b + (delta)**0.5) / (2 * a)  # Primeira raiz
        raiz2 = (-b - (delta)**0.5) / (2 * a)  # Segunda raiz
        
        tad['raiz1'] = raiz1
        tad['raiz2'] = raiz2

# Função para obter a primeira raiz
def getRaiz1(tad):
    if quant_raizes(tad) > 0:
        return tad['raiz1']
    return None

# Função para obter a segunda raiz
def getRaiz2(tad):
    if quant_raizes(tad) > 1:
        return tad['raiz2']
    return None

# Exemplo de uso:

# Criando a equação 2x² - 4x - 6 = 0
eq = new_eq(2, -4, -6)

# Acessando os coeficientes
print(f"Coeficiente A: {getA(eq)}")
print(f"Coeficiente B: {getB(eq)}")
print(f"Coeficiente C: {getC(eq)}")

# Calculando as raízes
calcular_raizes(eq)

# Verificando o número de raízes
print(f"Número de raízes: {quant_raizes(eq)}")

# Obtendo as raízes
raiz1 = getRaiz1(eq)
raiz2 = getRaiz2(eq)
if raiz1 is not None:
    print(f"Raiz 1: {raiz1}")
if raiz2 is not None:
    print(f"Raiz 2: {raiz2}")

# Atualizando a equação para 1x² - 3x + 2 = 0
new_eq(1, -3, 2)

# Exemplo com a nova equação
print("\nApós atualizar a equação para 1x² - 3x + 2 = 0:")
print(f"Coeficiente A: {getA(eq)}")
print(f"Coeficiente B: {getB(eq)}")
print(f"Coeficiente C: {getC(eq)}")

# Calculando as raízes
calcular_raizes(eq)
print(f"Número de raízes: {quant_raizes(eq)}")
print(f"Raiz 1: {getRaiz1(eq)}")
print(f"Raiz 2: {getRaiz2(eq)}")
