# aula 14
# lista e dicionário
nomes = ["Pedro", "Ceci", "Luciano", "Clarisse", "Patrícia"]
numeros = [[81991919092],[81989380990], [81998062019], [81993009093], [81991080972]]
numero_de_ceci = numeros[nomes.index("Ceci")]
print(numero_de_ceci)


# para o dicionário usa-se as chaves {}
# as chaves são separadas de seus valores por dois pontos
agenda = {"pedro": [81991919092], "maria": [1212]}
print(agenda["maria"])

# até então dicionário é mais simples que as listas para verificar valores (nomes e números), relacionar os dois
# dicionário = {"nome": [número], "nome_2":[número_2]}

# adicionando valores
dicionario = {}
for i in range(3):
    nome = input("Digite um nome: ")
    telefone = int(input(f"Digite o telefone de {nome}: "))
    dicionario[nome] = telefone
print(dicionario)

dic = {}
while True:
    continuar = input("Deseja continuar (SIM/NÃO)? ").upper()
    if continuar == "NÃO" or continuar == "NAO":
        print ("Encerrando.")
        break
    elif continuar == "SIM":
        nom = input("digite um nome: ")
        tele = int(input(f"Digite o telefone de {nom}: "))
        dic[nom] = tele
    else:
        print("Resposta inválida")
print(dic)



# deletando --- del "chave"
agenda_B = {"pedro": [81991919092], "maria": [81989300990]}
del agenda_B ["maria"]
print(agenda_B)
print(len(agenda_B)) # conta quantos elementos tem no dicionário criado

# verificar --- in , .values()
# verificar item: obs: ainda não é aquela função item que andré usa
moedas = {"maria": 23, "carlos": 33}
print("maria" in moedas) # True
print("carlos" in moedas ) # True
print(23 in moedas) #False
print(23 in moedas.values()) #True, para verificar se um número é verdadeiro, usa-se a função .values()

# acessar --- .items()
# para acessar um item no dicionário, voc~e usa items()
# voce acessa todos os valores, e não só um específico
notas = {"pedro": [9.2, 8.4, 4.3], "andre": [9.8, 9.7, 9.2]}
print(notas.items()) # vai acessar todas as notas

# acesar --- .keys()
# ele vai acessar somente os nomes, e não os números
print(notas.keys())

# acessar --- .values()
# acessa somente os numeros
print(notas.values())


brinquedos = {}
produto = input("Digite o produto: ")
quantidade = int(input("digite a quantidade: "))
brinquedos[produto] = quantidade
print(brinquedos)

for produto, quantidade in brinquedos.items(): # voce não precisa atribuir valores as variáveis antes, porque o próprio for ja faz isso
    print(produto, quantidade) # o python não sabe que o produto significa brinquedo nem nada, ele apenas respeita a ordem qe você colocou
    # oque importa é a posição da variável, e não o seu nome
