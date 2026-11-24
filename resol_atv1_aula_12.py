# atividade de matriz, criar uma matriz 3x3
# somar todos os valores ímpares
# somar os valores da primeira coluna
# mostrar qual o menor valor da terceira linha

# obs: linhas ficam na horizontal, colunas na vertical

matriz = []
for i in range (3):
    linha = []
    for j in range (3):
        num = int(input(f"Digite um número para a [{i+1}][{j+1}]: "))
        linha.append(num)
    matriz.append(linha)
print("\n=== matriz 3x3 ===")
for linha in matriz:
    print(linha)
