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
