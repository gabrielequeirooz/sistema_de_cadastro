# Lista para armazenar os alunos
alunos = []

while True:
    print("\n--- SISTEMA DE CADASTRO DE ALUNOS ---")
    print("1 - Inserir aluno")
    print("2 - Consultar aluno")
    print("3 - Alterar aluno")
    print("4 - Remover aluno")
    print("5 - Listar todos")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    # INSERIR
    if opcao == "1":
        while True:
            nome = input("Nome: ")
            if nome.replace(" ", "").isalpha():
                break
            else:
                print("Digite apenas letras no nome.")

        idade = input("Idade: ")
        curso = input("Curso: ")
        matricula = input("Matrícula: ")

        aluno = {
            "nome": nome,
            "idade": idade,
            "curso": curso,
            "matricula": matricula
        }

        alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")

    # CONSULTAR
    elif opcao == "2":
        matricula = input("Digite a matrícula para buscar: ")
        encontrado = False

        for aluno in alunos:
            if aluno["matricula"] == matricula:
                print(aluno)
                encontrado = True
                break

        if not encontrado:
            print("Aluno não encontrado.")

    # ALTERAR
    elif opcao == "3":
        matricula = input("Digite a matrícula para alterar: ")
        encontrado = False

        for aluno in alunos:
            if aluno["matricula"] == matricula:
                
                while True:
                    novo_nome = input("Novo nome: ")
                    if novo_nome.replace(" ", "").isalpha():
                        break
                    else:
                        print("Digite apenas letras no nome.")

                aluno["nome"] = novo_nome
                aluno["idade"] = input("Nova idade: ")
                aluno["curso"] = input("Novo curso: ")

                print("Aluno alterado com sucesso!")
                encontrado = True
                break

        if not encontrado:
            print("Aluno não encontrado.")

    # REMOVER
    elif opcao == "4":
        matricula = input("Digite a matrícula para remover: ")
        encontrado = False

        for aluno in alunos:
            if aluno["matricula"] == matricula:
                alunos.remove(aluno)
                print("Aluno removido com sucesso!")
                encontrado = True
                break

        if not encontrado:
            print("Aluno não encontrado.")

    # LISTAR
    elif opcao == "5":
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            for aluno in alunos:
                print(aluno)

    # SAIR
    elif opcao == "6":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")