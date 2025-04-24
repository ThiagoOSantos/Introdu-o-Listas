'''def mostrar_nomes():
    nomes = ["Mauri", "Clara-tiktoker", "bella-do-grau", "Danilo-fofoqueiro", "Thiago", "Jonhy Green"]
    print("Lista de nomes: \n")
    for nome in nomes:
        print(nome)

mostrar_nomes()

def media_notas():
    notas =[5.9, 8.5, 9.9, 9.7]
    media = sum(notas) / len(notas) #sum é uma função q soma os elementos de uma lista e o len( de lenght ) está sendo usado para dividir pelo tamanho da lista,
     para exibir o tamanho de uma lista usa-se o 'lista'.len
    print(f"As notas existentes são:\n {notas}")
    print(f"A média final é:\n {media:.2f}")

media_notas()'''
def cadastrar_produtos():
    produtos = []
    while True:
        produto = input("Digite o nome do produto ou digite 'sair' para encerrar:\n")
        if produto.lower() == "sair":
            break
        produtos.append(produto) #Para adicionar produtos em uma lista, usei 'append' para acrescenter esse item na ultima posição
        #Composição do comando: nome_da_lista.comando(variavel)
    print(f"Produtos cadastrados:\n {produtos}")

cadastrar_produtos()
