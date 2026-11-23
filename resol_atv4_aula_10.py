# RESOLUÇÃO DA ATIVIDADE 4 DA AULA 10
# usado o chatgpt para criação do código de forma mais simples

votos = []

while True:
    num = int(input("Digite o número da camisa (7-11): "))

    if num == 0:
        break
    elif num < 7 or num > 11:
        print("Número inválido, tente de novo!")
    else:
        votos.append(num)

total = len(votos)

print(f"\nForam computados {total} votos.")

if total > 0:
    maior = 0
    vencedor = 0

    print("\nJogador | Votos | %")

    for jogador in range(7, 12):
        quantidade = votos.count(jogador)
        percentual = quantidade / total * 100

        print(f"{jogador}       | {quantidade}     | {percentual:.1f}%")

        if quantidade > maior:
            maior = quantidade
            vencedor = jogador

    percentual_vencedor = maior / total * 100

    print(f"\nO melhor jogador foi o número {vencedor}, "
          f"com {maior} votos, correspondendo a "
          f"{percentual_vencedor:.1f}% do total de votos.")
else:
    print("Nenhum voto válido foi registrado.")
