#ATIVIDADE DA AULA 8:
#contar se o número é perfeito ou não:
#OBS: ESSA EU NÃO ENTENDI MUITO BEM.
num = int(input("Digite um número: "))
soma = 0
for i in range (1, num):
    if num % i == 0:
        soma = soma + i

if num == soma:
    print ("O número", num, "é perfeito")
else:
    print ("o número", num, "não é perfeito")