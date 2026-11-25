# atividade 3 da aula 14
estoque = {}
produtos = int(input("Quantos produtos vão ser cadastrados? "))
for i in range(produtos):
    print(f"\nproduto {i+1}") # não entendi esse i+1
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: "))
    estoque[nome]=[quantidade, preco]
print("\n")
for produto in estoque:
    print(f"{produto}: {estoque[produto][0]} unidades") # não entendi essa linha, nem o [0]
print("\n")
for produto in estoque:
    valor_total = estoque[produto][0] * estoque[produto][1] # não entendi essa linha, nem [0][1]
    print(f"Valor total de {produto}: R$ {valor_total:.2f}")
