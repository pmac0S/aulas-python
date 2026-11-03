#atividade da aula 8
#petshopp
print("===Bem vindo ao petshopp!===")
banho = 0
tosa = 0
banho_tosa = 0
outros = 0
for i in range (5):
    nome = input("Informe o nome do seu cachorro: ")
    serviço = int(input("Informe o serviço desejado (1-banho; 2-tosa; 3-banho e tosa; 4-outros): "))
    if serviço == 1:
        banho += 1
    elif serviço == 2:
        tosa += 1
    elif serviço == 3:
        banho_tosa += 1
    elif serviço == 4:
        outros += 1
    else:
        print ("Serviço inválido)")
        break
print (f"A quantidade de banhos foi de: {banho}")
print (f"A quantidade de tosas foi de: {tosa}")
print (f"A quantidade de banhos e tosas foi de: {banho_tosa}")
print (f"A quantidade de outros foi de: {outros}")

