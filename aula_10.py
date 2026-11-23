# ESTRUTURA DE DADOS (listas):
# ajudam a armazenar uma grande quantidade de informções na memória ao mesmo tempo
# ela faz conexão direta com estruturas de repetiçã
# obs: estrutura de dados ≠ estrutura de repetição
num = [1, 2, 5, 9]
print (num)
num.append(2) # .append adiciona algo na lista criada


frutas = ["maçã", "banana", "morango"]
print (frutas)
frutas.append("uva")


valores = []
for i in range(5):
    valores.append(int(input("Digite um valor: "))) # nota-se que para escrever o int, você não preciso digitar o sinal de = antes
    print(valores)
# você pode lietralmente só guardar valores que o usuario vai inserir
# a lista  vai mostrando os valores que você colocou (entenda valores não apenas como sendo só números)
# usar o .append() serve para literalmente guadar os valores que o usuário digitar na lista
# é como se ele pegasse o valor e já colocasse direto na lista criada
# funções usadas: len(), .append(), .sort()
# algumas funções adicionais: min(), max(), sum()

notas = []
for i in range (1, 6):
    notas.append(int(input(f"Digite a {i} nota: ")))
    notas.sort()

print(notas)
print(f"A menor nota foi: ", min(notas))
print(f"A maior nota foi: ", max(notas))
print(f"A soma das notas foi: ", sum(notas))
