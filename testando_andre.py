# 25/11/26
# hoje na aula André me ensinou como achar um nome vinculado a um número em ma lista (usando index)
nome = []
idade = []
while True:
    continuar = input("Deseja continuar? (SIM/NÃ0) ").upper()
    if continuar == "SIM":
        nom = input("Adiciona nome: ")
        id = int(input("Adicionar idade: "))
        if id < 18:
            print ("Idade não autorizada.")
        else:
            nome.append(nom)
            idade.append(id)
    elif continuar == "NÃO" or continuar == "NAO":
        print("Encerrando programa.")
        break
    else:
        print("Resposta inválida.")


acessar = input("Qual nome deseja acessar? ")

if acessar in nome:
    acessar_nome = nome.index(acessar)
    print(f"Nome: {nome[acessar_nome]}")
    print(f"Idade: {idade[acessar_nome]}")
else:
    print("Nome não relacionado")
