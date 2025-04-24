def lista_int():
    listaint = []
    listapar = []
    for i in range(6):
        lista = int(input("digite 1 numero: \n"))
        if lista % 2 == 0:
            listapar.append(lista)
        else:
            listaint.append(lista)
    media1 = sum(listaint)
    mediapar = sum(listapar)
    print("Os valores da lista ímpar são:\n")
    print(media1)
    print("Os valores da lista par são:\n")
    print(mediapar)

lista_int()