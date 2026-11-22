#ATIVIDADE DA AULA 9:
#CRIAR UMA URNA PARA OS BRUXOS
harry = 0
hermione = 0
branco = 0
while True:
    votos = int(input("Digite o seu candidato (1 = Harry Potter, 2 = Hermione Granger, 3 = Branco, 4 = Encerrar): "))
    if votos == 4:
        break
    elif votos == 1:
        harry += 1
    elif votos == 2:
        hermione += 1
    elif votos == 3:
        branco += 1
    else:
        print("Voto não computado!")

total = harry + hermione + branco

if total > 0:
    porcentagem = branco / total *100
else:
    porcentagem = 0

if harry > hermione:
    print("O vencedor foi Harry Potter!")
elif hermione > harry:
    print("A vencedora foi Hermione Granger!")
else:
    print("Houve um empate técnico!")

print(f"O número total de votos foi de {total}")
print(f"O número de votos para Harry foi {harry}.")
print(f"O número de votos para Hermione foi {hermione}.")
print (f"A porcentagem de votos brancos foi de {porcentagem:.2f}%")
