# atividade da aula 12
# criar uma matriz 3x3
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Digite um número para [{i+1}][{j+1}]: "))
        linha.append(num)
    matriz.append(linha)
print("\n=== matriz 3x3 ===")
for linha in matriz:
    print(linha)


# matriz = []
# for i in range(3):
# linha = []
# for j in range(3):
# num = int(input("Digite um número para [{i+1}][{j+1}]: "))
# linha.append(num)
# matriz.append(linha)
# print("\n=== matriz 3x3 ===")
# for linha in matriz:
# print(linha)
