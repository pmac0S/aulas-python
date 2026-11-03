#atividade da aula 8, parque de diversões:
visitantes = int(input("informe a quantidade de visitantes: "))
maxima = float(input("informe a altura máxima (m): "))
minima = float(input("informe a altura mínima (m): "))
permitidos = 0
bloqueados = 0
for i in range (1, visitantes+1): #(1, visitantes + 1) para que o python entenda que a quantidade de visitantes seja a quantidade de vezes que o loop será executado, e o +1 é para que o loop seja executado a quantidade de vezes que o usuário informou, pois se não colocar o +1 o loop será executado somente uma vez.
    altura = float(input(f"informe a altura do visitante {i} (m): "))
    if minima <= altura <= maxima:
        permitidos += 1
    else:
        bloqueados += 1
print (f"O número de visitantes permitidos a entrara na montanha russa é: {permitidos}")
print (f"O número de visitantes bloqueados a entrar na montanha russa é: {bloqueados}")

#ENTENDI O CÓDIGO, MAS NÃO FAZ SENTIDO TER QUE COLOCAR A ALTURA MÍNIMA E MÁXIMA, O PRÓPRIO ESTABELECIMENTO TENQUE DIZER QUAL É A ALTURA MÍNIMA E MÁXIMA, POIS O USUÁRIO NÃO SABE.




    