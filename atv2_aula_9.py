#atividade 2 da aula 9:
valores = 0
while True:
    valor = int(input("Insira o valor do produto: "))
    if valor == 0:
        break
    elif valor < 0:
        print("inválido")
    else:
        valores += valor
total = valores + valor
if total > 1000:
    total * 0.10 #Parte errada, o certo seria: *0.9,
print(f"O valor total a pagar é de R${total:.2f}")
