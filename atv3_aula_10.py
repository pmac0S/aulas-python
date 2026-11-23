# Atividade 3 da aula 10
print("\n=== ATIVIDADE 3 ===")
peso = []
quantidade = int(input("Digite a quantidade de produtos vendidos: "))
for i in range (quantidade):
    peso.append(float(input(f"Digite o peso do produto {i} (kg): ")))
    soma = sum(peso)
    media = soma/quantidade
print(f"O peso médio dos produtos vendidos foi de: {media:.2f}kg.")
print(f"O maior peso vendido foi de: {max(peso)}kg.")
print(f"O menor peso vendido foi de: {min(peso)}kg.")
print(f"O total arrecadado foi de: R${soma*4.35:.2f}")
