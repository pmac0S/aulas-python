# aula 13
# string
# basicamente se faz contagem com string, cada palavra tem uma sequencia de números positivos e negativos
# esquerda para direita = positivos
# direita para esquerda = negativos

teste = "pedro"
teste[::-1]
print (teste) # mostrar o nome pedro no terminal
print(teste[::-1]) # mostrar as letras de tras para frente do nome pedro

print(len(teste)) # len é uma função de contagem, aqui ela contou quantas letras tem a variável teste ("pedro")

teste_2 = "Aprendendo python" # lembre-se que o len tbm vai contar com o espaço entre "aprendendo" e "python"
print(teste_2)
print(teste[::-1])
print(len(teste_2))

# até aqui você só fez contagem de caracteres
# mas você pode achar um caractere específico, ou uma sequencia de caracteres
caracteres = "Galega da boa"
print("lega" in caracteres) # true

gelo = "Geladinha"
print("gel" in gelo) # false

# CONCATENAÇÃO
nome = "Irineu"
sobrenome = "você não sabe nem eu"
print(f"{nome}, {sobrenome}")
print(nome, sobrenome)
print(nome +"," + sobrenome)

# REPLACE
# é um método de substituiçlão de caracteres
mudanca = "vamos mudar o código"
mudanca.replace("vamos", "eu")
print(mudanca)

mudamos = "mudarei o código!"
novo = mudamos.replace("mudarei", "mudei")
print(novo)

# algumas string:
# .upper(): deixa as letras maiúsculas
# .lower(): deixa as letras minúsculas
# .capitalize(): deixa só a primeira letra maiúscula
# .title(): deixa a primeira letra de todas maiúsculas
# .count(): escolhe um único caractere para ver quantas vezes aparece

letra = "letra da frase"
nova_letra = letra.capitalize()
print(nova_letra)

again = "new letter in speech"
print(again.upper()) # deixa tudo maiúsculo
print(again.lower()) # deixa tudo minúsculo
print(again.capitalize()) # deixa maiúscula só a primeira letra da frase
print(again.title()) #deixa todas as primeiras letras maiúsculas
print(again.count("e")) # seleciona um caractere para quantas vezes ele se repete
