brinquedos = {}
for i in range (3):
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("digite a quantidade do produto: "))
    brinquedos[nome] = quantidade
print("\n=== brinquedos cadastrados ===")
for produto, qtd in brinquedos.items():
    print(f"produtos: {produto}")
    print(f"quantidade: {qtd}")
    print("----------------")
