def notasturma():
    media = 0
    notasgeral = []
    #acimamedia = []
    aprovados = 0
    quantalunos = int(input("Digite quantos alunos tem na turma: \n"))
    for i in range (quantalunos):
        for j in range(4):
            nota = float(input("Digite as notas dos alunos: \n"))
            notasgeral.append(nota)
            media += nota
        if (media/4) >= 7:
            aprovados +=1

        mediaturma= sum(notasgeral)/ len(notasgeral)
    print(f"Essas são as notas da turma: \n {notasgeral}")
    print(f"A media da turma é de: {mediaturma}")
    print(f"{aprovados} estudantes ficaram acima da média")

notasturma()




'''    notasgeral = []
    quantinota = 4
    media_sete = 0
    quantalunos = int(input("Digite quantos alunos tem na turma: \n"))
    for i in range (quantalunos):
        media = 0
        for j in range (quantinota):
            media += float(input(f"Digite as notas {j+1} dos alunos: {i+1} \n"))
            media /= quantinota
            notasgeral.append(media)
            if media >= 7:
                media_sete += 1
       # print("\n A media de alunos foi: ")
    for i in range(quantalunos):
        print(f"Aluno {i+1} teve media de {notasgeral[i]}")
    print(f"{media_sete} alunos tiveram nota acima ou igual a média 7")

notasturma()'''