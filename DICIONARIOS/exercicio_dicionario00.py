# Exercício de dicionários

# Chave/Key - Valor/Valus
carro={"Fabricante":"Honda", "Modelo":"HRV", "Ano":"2021", "Cor":"Prata"}
carro["Cambio"]="Automático" # Adicionando uma nova CHAVE
carro.pop("Cambio") # Remover uma CHAVE OU del carro["Cambio"]


fab=carro.get("Fabricante") # OU fab=carro["Fabricante"] fazem a mesma coisa (acessar à chave)

carro["Cor"]="Preto" # Alterando o (VALOR)
print("Tamanho do Dictionary: " + str(len(carro)))
#carro.clear() # Para limpar os elementos

# Verificar se a chave 'modelo' existe no dicionário
if "Cor" in carro:
    print("Sim, é uma chave!\n")
else:
    print("Não é uma CHAVE, é um VALOR!")

#for x in carro:
#    print(x) # Imprimir chave
 #   print(carro[x]) # Imprimir valor 

for c,v in carro.items():  # Usa .items() para obter chave e valor
    print(c + ": " + v)



# Pode fazer das duas maneiras acima!!
    