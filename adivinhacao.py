import random
import os
import sys
import msvcrt

os.system("cls")

chances = 5
dif = 1
chancesextras = 0
acertos = 0

while chances > 0 and dif <= 6:
    os.sys("cls")
    if dif == 1:
        ran = random.randint(1, 2)
    elif dif == 2:
        ran = random.randint(1, 4)
    elif dif == 3:
        ran = random.randint(1, 5)
    elif dif == 4:
        ran = random.randint(1, 10)
    elif dif == 5:
        ran = random.randint(1, 20)
    elif dif == 6:
        ran = random.randint(1, 50)

    print(f"\nVocê tem {chances} chances.")
    print(f"Você acertou {acertos} vezes.")
    print(f"Dificuldade atual: {dif}")
    print("Precione qualquer tecla para jogar.")
    tecla = msvcrt.getch().decode('utf-8').lower()
    
    if tecla == "t":
        dicas = [
            f"O número é menor que {ran + 10}",
            f"O número é menor que {ran + 5}",
            f"O número é menor que {ran + 20}",
            f"O número é maior que {ran - 10}",
            f"O número é maior que {ran - 5}",
            f"O número é maior que {ran - 20}"
        ]
        print("💡 Dica:", random.choice(dicas))
    elif tecla == "r":
        dif = 1
        chances = 5
        acertos = 0
        os.system("cls")
        continue
    elif tecla == "q":
        print("Saindo do jogo...")
        sys.exit()
    d = input("Você quer jogar? (s/n) ").lower()
    if d in ["n", "nao", "não"]:
        print("Jogo encerrado.")
        sys.exit()
    elif d not in ["s", "sim"]:
        print("Resposta inválida!")
        continue

    os.system("cls")

    r = int(input("Digite o número: "))
    if r == ran:
        print("🎉 Certa resposta!")
        dif += 1
        acertos += 1
        if acertos == 2:
            chancesextras += 1
    else:
        print(f"Você errou. O número era {ran}.")
        chances -= 1

print("Suas chances acabaram.")