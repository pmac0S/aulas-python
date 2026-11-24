# aula 11:
# falaremos de matrizes. eLas são "funções" bidimensionais, representam uma tabela de linhas e colunas.
vetor = []
for i in range(5):
    vetor.append(int(input(f"Digite um valor para a posição {i}; ")))
print(vetor[2])

# basicamente você criou uma lista;
#  depois usou uma estrutura de repetição tipo for;
#  ai pediu para que o usuáro adcionasse um valor para a posição "i" na lista, usopu o .append() para os vaores serem adcionados na lista
# terminou com um print mostrando qual foi o valor escolhido na posição 2 da lista

matriz = []
for i in range(2):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para a posição [{i+1}][{j+1}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz 2x4:")
for linha in matriz:
    print(linha)

# é a mesma matriz em matemática, aquelas colunas e linhas!
