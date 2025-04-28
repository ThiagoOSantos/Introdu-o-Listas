def tarefas():
    tarefas = []
    while True:
        print("O que deseja fazer?")
        opcao = input("1 - Adicionar tarefa\n2 - Listar tarefa\n3 - Remover tarefa \n4 - sair \n")
        if opcao == "1":
            tarefa = input("qual a tarefa?\n")
            tarefas.append(tarefa)
        elif opcao == "2":
            print(tarefas)
        elif opcao == "3":
            remover = int(input("qual tarefa quer remover?\n"))
            tarefas.pop(remover)
        elif opcao == "4":
            break

tarefas()