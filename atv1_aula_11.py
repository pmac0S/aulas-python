# matriz 3x3
matriz = []
for i in range(3):
    linha = []
    for j in range (3):
        valor = int(input(f"Digite um valor para a posição [{i+1}][{j+1}]: "))
        linha.append(valor)
    matriz.append(linha)
print("\n=== Matriz 3x3 ===")
for linha in matriz:
    print(linha)

# a) A soma de todos os valores ímpares;
# b) A soma dos valores da primeira coluna;
# c) O menor valor da terceira linha.
