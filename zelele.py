# Recapitulando aula 10
# aprendendo matriz
# funções de listas: .append(), .sort(), len(), max(), min(), sum), .pop(),

# o código abaixo é um código interativo, organizado, onde o usuário vai escolher no terminal determinada função a partir de um print pré-especificado:

nomes = []
while True:
    print("\n=== Menu de Opções ===")
    print("1.Adicionar nome")
    print("2.Listar nomes")
    print("3.Atualizar nome")
    print("4Deletar nome")
    print("5.Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        nomes.append(input("Digite o nome que deseja adicionar: "))

    elif opcao == 2:
        print("Lista de nomes: ")
        for i in enumerate(nomes):
            print(f"{i+1} nome: {nome}")

    elif opcao == 3:
        indice = int(input("digite o índice do nome que deseja atualizar: ")) - 1
        if 0 <= indice < len(nomes):
            novo_nome = input(f"Digite o novo nome: ")
            nomes[indice] = novo_nome
        else:
            print("Índice inválido.")
    elif opcao == 4:
        indice = int(input("Digite o índice do nome que deseeja deletar: ")) - 1
        if 0 <= indice < len(nomes):
            nomes.pop(indice)
        else:
            print("Índice unválido.")
    elif opcao == 5:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")
