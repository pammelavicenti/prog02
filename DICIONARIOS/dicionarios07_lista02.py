# Caminho do arquivo que armazenará os contatos
arquivo = "agenda.txt"

# Função para carregar os contatos do arquivo
def carregar_contatos():
    contatos = {}
    try:
        with open(arquivo, "r") as f:
            for linha in f:
                numero, nome = linha.strip().split(",")
                contatos[numero] = nome
    except FileNotFoundError:
        pass  # Se o arquivo não existe, retorna uma agenda vazia
    return contatos

# Função para salvar os contatos no arquivo
def salvar_contatos(contatos):
    with open(arquivo, "w") as f:
        for numero, nome in contatos.items():
            f.write(f"{numero},{nome}\n")

# Função para adicionar um novo contato
def adicionar_contato(numero_telefone, nome_contato):
    contatos = carregar_contatos()
    
    if numero_telefone in contatos:
        print(f"Erro: O número {numero_telefone} já está cadastrado.")
    else:
        contatos[numero_telefone] = nome_contato
        salvar_contatos(contatos)
        print(f"Contato de {nome_contato} adicionado com sucesso!")

# Função para remover um contato
def remover_contato(numero_telefone):
    contatos = carregar_contatos()
    
    if numero_telefone in contatos:
        del contatos[numero_telefone]
        salvar_contatos(contatos)
        print(f"Contato removido com sucesso!")
    else:
        print(f"Erro: O número {numero_telefone} não foi encontrado na agenda.")

# Função para buscar um contato
def buscar_contato(numero_telefone):
    contatos = carregar_contatos()
    
    if numero_telefone in contatos:
        print(f"{numero_telefone}: {contatos[numero_telefone]}")
    else:
        print(f"Erro: O número {numero_telefone} não foi encontrado na agenda.")

# Função para exibir todos os contatos
def exibir_contatos():
    contatos = carregar_contatos()
    
    if not contatos:
        print("A agenda está vazia.")
    else:
        print("Contatos da agenda:")
        for numero, nome in sorted(contatos.items(), key=lambda x: x[1]):
            print(f"{numero}: {nome}")

# Exemplo de uso
adicionar_contato("987654321", "Carlos")
adicionar_contato("123456789", "Ana")
exibir_contatos()
buscar_contato("987654321")
remover_contato("987654321")
exibir_contatos()
