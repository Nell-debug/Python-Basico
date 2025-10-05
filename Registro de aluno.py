alunos = {
    "José": 8,
    "Júlia": 10,
    "Davi": 5
}
while True:   # Loop
    print("Lista atual de alunos:")
    for dic in alunos:
        print(dic)
    print("-" * 30)
    Entrada = input("Deseja editar o registro de alunos? (s/n) ").lower()

    if Entrada in ["s", "sim"]:
        print("-" * 30)
        print("Opções disponíveis:")
        print("(1) Ver notas")
        print("(2) Edição de nota")
        print("(3) Edição de nome")
        print("(4) Remoção de aluno")
        print("(5) Adição de aluno")
        print("-" * 30)

        opcao = input("O que deseja fazer? ")
        print("-" * 30)

        if opcao == "1":
            for aluno, nota in alunos.items():
              print(f"Aluno - {aluno} | Nota - {nota}")

            inicio = input("deseja voltar ao início?(s/n) ").lower()
            if inicio in ["s","sim"]:
             print("-" * 30)
             continue
            else:
              break

        elif opcao == "2":
            print("(1)José")
            print("(2)Júlia")
            print("(3)Davi")
            edit = input("A nota de qual aluno você deseja editar? ")
            if edit == "1":
                nova_nota = int(input("Digite a nova nota do aluno: "))
                alunos["José"] = nova_nota
                print("-" * 30)
            elif edit == "2":
                nova_nota = int(input("Digite a nova nota do aluno: "))
                alunos["Júlia"] = nova_nota
                print("-" * 30)
            elif edit == "3":
                nova_nota = int(input("Digite a nova nota do aluno: "))
                alunos["Davi"] = nova_nota
                print("-" * 30)
            else:
                print("Opção inválida!")
                continue

        elif opcao == "3":
            print("-" * 30)
            print("(1)José")
            print("(2)Júlia")
            print("(3)Davi")
            edit_nome = input("O nome de qual aluno você deseja editar? ")
            if edit_nome == "1":
                novo_nome = input("Digite o novo nome do aluno(a): ")
                alunos[novo_nome] = alunos.pop("José")
                print("-" * 30)
            elif edit_nome == "2":
                novo_nome = input("Digite o novo nome do aluno(a): ")
                alunos[novo_nome] = alunos.pop("Júlia")
                print("-" * 30)
            elif edit_nome == "3":
                novo_nome = input("Digite o novo nome do aluno(a): ")
                alunos[novo_nome] = alunos.pop("Davi")
                print("-" * 30)
            else:
                print("Opção inválida!")
                continue

        elif opcao == "4":
            print("-" * 30)
            print("(1)José")
            print("(2)Júlia")
            print("(3)Davi")
            remove = input("Qual aluno deseja remover? ")
            print("-" * 30)
            if remove == "1":
                del alunos["José"]
            elif remove == "2":
                del alunos["Júlia"]
            elif remove == "3":
                del alunos["Davi"]
            else:
                print("Aluno não encontrado")

        elif opcao == "5":
            print("-" * 30)
            novo_aluno = input("Digite o nome e a nota do novo aluno: ")
            partes_aluno = novo_aluno.split()
            if len(partes_aluno) == 2:
                nome = partes_aluno[0]
                nota = int(partes_aluno[1])
                alunos[nome] = nota
            else:
                print("Opção inválida!")

        else:
            print("Opção inválida!")
            print("-" * 30)

    else:
        print("Encerrando o programa...")
        print("-" * 30)
        break