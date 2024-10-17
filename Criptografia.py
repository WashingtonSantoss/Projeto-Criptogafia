import random
import string

#Declarando funções 

# Função para criptografar

def criptografar(texto, chave):
    criptografado = []
    for i in range(len(texto)):
        criptografado.append(texto[i] ^ chave[i % len(chave)])
    return bytes(criptografado)

# Função para gerar uma chave aleatoria e associar com uma chave 'string'

def criar_chave_aleatoria(nome_chave):
    random_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
    chaves[nome_chave] = random_key.encode('utf-8')
    salvar_chaves()

# Função que gera e salva as chaves em um arquivo '.txt'

def salvar_chaves():
    with open("chaves.txt", "w") as arquivo:
        for chave_nome, chave in chaves.items():
            arquivo.write(f"{chave_nome}:{chave.hex()}\n")

# Função para verificar a chave

def buscar_chave(nome_chave):
    if nome_chave in chaves:
        return chaves[nome_chave]
    try:
        return bytes.fromhex(nome_chave)
    except ValueError:
        return None

# Dicionario criado para armazenar as chaves

chaves = {}

# Abrindo o arquivo para verificar se a chave existe
try:
    with open("chaves.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            partes = linha.strip().split(":")
            if len(partes) == 2:
                chave_nome, chave = partes
                chaves[chave_nome] = bytes.fromhex(chave)
except FileNotFoundError:
    pass

# fim do meu declare

# Aqui começa o programa

while True:
    print("\nOpções:")
    print("1. Criptografar")
    print("2. Criar Chave Aleatória")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        chave_nome = input("Nome da chave ou chave hexadecimal: ")
        chave = buscar_chave(chave_nome)

        if chave:
            mensagem = input("Insira a frase que deseja criptografar: ")
            if mensagem:
                mensagem_bytes = mensagem.encode('utf-8')
                mensagem_cifrada = criptografar(mensagem_bytes, chave)
                print("Frase criptografada:", mensagem_cifrada.hex())
            else:
                print("Nenhuma frase inserida. Operação de criptografia cancelada.")
        else:
            print("Chave não encontrada ou inválida.")
    elif opcao == '2':
        chave_nome = input("Nome da nova chave: ")
        if chave_nome not in chaves:
            criar_chave_aleatoria(chave_nome)
            print("Chave aleatória gerada e associada a", chave_nome)
        else:
            print("Já existe uma chave com esse nome.")
    elif opcao == '3':
        break
    else:
        print("Opção inválida. Tente novamente.")
