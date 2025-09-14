import os
import random
import sys

os.system("cls")

while True:
    os.system("cls")
    i = input("Par ou ímpar? ").lower()

    os.system("cls")

    if i in ["impar", "ímpar"]:
        print("Você escolheu ímpar, então o programa escolhe par.")
        resposta = int(input("Qual número ímpar você escolhe? "))
        os.system("cls")

        programa = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
        resposta1 = random.choice(programa)

        if resposta % 2 == 0:
            print("Erro! Você escolheu um número par.")
            print("Reiniciando o jogo...\n")
            continue
        else:
            print(f"Você: {resposta} | Programa: {resposta1}")
            final = (resposta + resposta1)
            if final % 2 != 0:
                print("O programa ganhou.")
            else:
                print("Parabéns! Você venceu.")
                r = input("Deseja jogar novamente? ").lower()
        if r in ["sim","s"]:
            print("Reiniciando o jogo...\n")
            continue
        elif r in ["não","n","nao"]:
            print("Encerrando o jogo...")
            sys.exit()
    elif i in ["par"]:
        print("Você escolheu par, então o programa escolhe ímpar.")
        resposta = int(input("Qual número par você escolhe? "))
        os.system("cls")

        programa = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
        resposta1 = random.choice(programa)

        if resposta % 2 != 0:
            print("Erro! Você escolheu um número ímpar.")
            print("Reiniciando o jogo...\n")
            continue
        else:
            print(f"Você: {resposta} | Programa: {resposta1}")
            final = (resposta + resposta1)
            if final % 2 != 0:
                print("O programa ganhou.")
            else:
                print("Parabéns! Você venceu.")
        r = input("Deseja jogar novamente? ").lower()
        if r in ["sim","s"]:
            print("Reiniciando o jogo...\n")
            continue
        elif r in ["não","n","nao"]:
            print("Encerrando o jogo...")
            sys.exit()
    else:
        print("Escolha inválida! Digite 'par' ou 'impar'.")
