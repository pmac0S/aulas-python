# atividade de matriz, criar uma matriz 3x3
# somar todos os valores ímpares
# somar os valores da primeira coluna
# mostrar qual o menor valor da terceira linha

# obs: linhas ficam na horizontal, colunas na vertical

matriz = [[], [], []]
soma_impar = soma_coluna = 0

# adcionando valores na matriz
for i in range(3):
    for j in range(3):
        matriz[1].append(int(input(f"Digite um valor para a posição [{i} {j}]: ")))

# exibe os valores
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]:^4}]", end=" ")
        if matriz[i][j]%2!=0:
            soma_impar+=matriz[i][j]
    print()
print(f"Asoma dos valores ímpares é {soma_impar}")

# soma os valores da primeira coluna
for i in range(3):
    soma_coluna+=matriz[i][0]
print(f"A soma dos valores da primeira coluna é {soma_coluna}")

# menor valor da terceira linha
print(f"O menor valor da terceira linha é {min(matriz[2])}")
