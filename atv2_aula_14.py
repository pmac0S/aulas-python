cardapio = {"coxinha": [5.00], "pastel": [4.00], "suco": [3.50], "bolo": [4.50]}
print(cardapio)
while True:
    decisao = input("Deseja modificar o cardapio? (SIM/NÃO): ").upper()
    if decisao == "NAO" or decisao == "NÃO":
        print(cardapio)
        break
    elif decisao == "SIM":
        print("\n=== opções ===")
        print("A.remover")
        print("B.adicionar")
        print("C.modificar")
        opcao = input("Digite a opção escolhida: ").upper()
        if opcao == "A":
            remover = input("Digite o produto que deseja remover: ")
            if remover in cardapio:
                del cardapio [remover]
                print(cardapio)
            else:
                print("Produto não encontrado")
        elif opcao == "B":
            adicionar = input("Digite o produto que queira adicionar: ").lower()
            preco = float(input("Digite o preço do produto: "))
            cardapio[adicionar]=preco
            print(cardapio)
        elif opcao == "C":
            modificar = input("Digite o produto que queira modificar: ").lower()
            if modificar in cardapio:
                novo_preco = float(input("Digite o novo preço: "))
                cardapio[modificar]= novo_preco
                print(cardapio)
            else:
                print("Produto não encontrado")
    else:
        print("Opção inválida")
