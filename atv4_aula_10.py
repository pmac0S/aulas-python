# atividade 4 da aula 10:
jogador_7 = []
jogador_8 = []
jogador_9 = []
jogador_10 = []
jogador_11 = []
while True:
    num = int(input("Digite o número da camisa (7-11): "))
    if num == 0:
        break
    elif num < 7 or num > 11:
        print("Número inválido, tente de novo!")
    elif num == 7:
        jogador_7.append(num)
    elif num == 8:
        jogador_8.append(num)
    elif num == 9:
        jogador_9.append(num)
    elif num == 10:
        jogador_10.append(num)
    elif num == 11:
        jogador_11.append(num)
print(f"O total de votos válidos: {len(jogador_7)+len(jogador_8)+len(jogador_9)+len(jogador_10)+len(jogador_11)}")
