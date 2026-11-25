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
