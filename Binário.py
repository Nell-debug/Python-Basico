print("(1)Codificar \n(2)Decodificar")
binario = input("O que você deseja fazer? ").lower()
if binario == "1":
    entrada = input("Digite a informação a ser codificada: ")
    lista = []
    for caractere in entrada:
        num = ord(caractere)
        binario = bin(num)[2:]
        lista.append(binario)
    print(" ".join(lista))
elif binario == "2":
    entrada = input("Digite a informação a ser decodificada: ")
    blocos = entrada.split()
    lista = []
    for bloco in blocos:
        num = int(bloco, 2)
        char = chr(num)
        lista.append(char)
    print(" ".join(lista))