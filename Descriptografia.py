
#Declarando funcões 

# Funçaõ de descriptografia

def input_mensagem_cifrada_hex():
    while True:
        mensagem_cifrada_hex = input("Insira a frase criptografada em hexadecimal: ")
        if is_hexadecimal(mensagem_cifrada_hex):
            return mensagem_cifrada_hex
        else:
            print("O texto inserido não é um valor hexadecimal válido. Tente novamente.")

def is_hexadecimal(texto):
    try:
        bytes.fromhex(texto)
        return True
    except ValueError:
        return False

# No seu loop principal, você pode chamar a função input_mensagem_cifrada_hex() para obter o texto criptografado em hexadecimal.
# Substitua esta linha:
# mensagem_cifrada_hex = input("Insira a frase criptografada em hexadecimal: ")

def descriptografar(textocriptografado, chave):
    descriptografado = []
    for i in range(len(textocriptografado)):
        descriptografado.append(textocriptografado[i] ^ chave[i % len(chave)])
    return bytes(descriptografado)

# Aqui eu verifico o valor da chave 'string' e mostro seu valro em hexadecimal

def buscar_chave(nome_chave):
    if nome_chave in chaves:
        return chaves[nome_chave]
    try:
        return bytes.fromhex(nome_chave)
    except ValueError:
        return None

# As chaves são mapeadas usando um dicionario python.

chaves = {}

# Aqui carrega o arquivo gerado no codigo de criptografia.

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

#Fim do meu declare.

# Aqui inicia meu programa.

while True:
    print("\nOpções:")
    print("1. Descriptografar")
    print("2. Verificar Chave")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        chave_nome = input("Nome da chave ou chave hexadecimal: ")
        chave = buscar_chave(chave_nome)

        if chave:
            mensagem_cifrada_hex = input_mensagem_cifrada_hex()
            mensagem_cifrada = bytes.fromhex(mensagem_cifrada_hex)
            mensagem_decifrada = descriptografar(mensagem_cifrada, chave)
            mensagem_decifrada_str = mensagem_decifrada.decode('utf-8', errors='ignore')
            print("Frase descriptografada:", mensagem_decifrada_str)
        else:
            print("Chave não encontrada ou inválida.")
    elif opcao == '2':
        chave_nome = input("Digite o nome da chave para verificar: ")
        if chave_nome in chaves:
            chave_bytes = chaves[chave_nome]
            print(f"Chave associada a {chave_nome}: {chave_bytes.hex()}")
        else:
            print("Chave não encontrada.")
    elif opcao == '3':
        break
    else:
        print("Opção inválida. Tente novamente.")




