

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i+1}][{j+1}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz 2x4:")
for linha in matriz:
    print(linha)

# é a mesma matriz em matemática, aquelas colunas e linhas!
