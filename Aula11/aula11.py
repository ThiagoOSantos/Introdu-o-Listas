#introdução a conjuntos com Python (: - Professor Mauricesarrrrrrrrrrrrrrrrrr
def conjunto_frutas():
    frutas = {"maçã","banana","laranja","uva"} #a definição de conjunto em python se da por chaves{}
    print("Essas são as frutas do meu conjunto: ")
    for fruta in frutas:
        print(f"- {fruta}")

# conjunto_frutas()

'''def lista_de_produtos():
    produtos = {
        "notebook": 3500,
        "chinelo": 25,
        "maçã": 8.5,

    }
    print("Meus Produtos: ")
    for produto in produtos.keys(): #pesquisar
        print(f"- {produto}") '''

def produtos_com_mais_coisas():
    produtos = {
        "notebook":("LG", 3500.00, "Cartão em até 12x com acréscimo"),
        "monitor": ("Samsung", 1400.00, "144hz", "Cartão em 6x sem juros"),
        "teclado": ("Logitech", 122.00, "A vista"),

    }
    print("Produtos cadastrados: ")
    for produto, detalhes, in produtos.items(): #produto foi interpretado como indice e detalhes como o conteúdo dentro do indice
        marca, preco, pagamento = detalhes
        print(f"Produto: {produto}")
        print(f" - Marca: {marca}")
        print(f" - Preço: {preco:.2f}")
        print(f" - Formas de Pagamento: {pagamento}")
produtos_com_mais_coisas()