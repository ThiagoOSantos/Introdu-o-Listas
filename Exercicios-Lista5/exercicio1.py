def cadastraonome():
    nomes = []
    while True:
        nome = input("Digite os nomes dos alunos ou 'sair' para encerrar o programa")
        if nome.lower() == "sair":
            break
        nomes.append(nome)
    print("Nomes cadastrados:\n")
    print(nomes)
cadastraonome()