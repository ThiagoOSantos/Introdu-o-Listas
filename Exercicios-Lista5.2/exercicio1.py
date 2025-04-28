def cidadesbr():
    cidades = []
    for i in range (3):
        cidades = input("Cite 8 cidades brasileiras: ")
    conjunto = set(cidades)
    print(f"Essas foram as cidades: {conjunto}")

cidadesbr()