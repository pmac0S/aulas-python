barato = 0
caro = 0
for i in range (10):
    distancia = float(input(" Informe a distância percorrida (km): "))
    tempo = int(input(" Informe o tempo (min): "))
    valor = (distancia * 2.50) + (tempo * 0.30)
    if valor > 30.00:
        caro += 1
        print (f"\n O valor da corrida é R${valor:.2f}")
    else:
        barato += 1
        print (f"\n O valor da corrida é R${valor:.2f}")
print(f" O total de corridas caras foi: {caro}")
print (f" O total de corridas baratas foi de: {barato}")


