#Anotações da aula 9:
#A aula 9 fala sobre estrutura de repetição (While), contador e acumulador
cont = 0
while cont <5:
    print (cont)
    cont += 1


idade = 0
for i in range (5):
    id = int(input("Digite a sua idade: "))
    soma = idade + id
    idade += id
print("A soma das idades é:", soma)



while True:
    num = int(input("Digite um número: "))
    if num == 0:
        print("Zero!")
        break
    elif num > 0:
        print("Número positivo!")
    else:
        print("Número negativo!")
print("Encerrando programa!")
