# primeira atividade da aula 13
frase = input("Frase: ")
palavra = input("Palavra da frase: ")
substituir = input("Palavra substituta: ")

if palavra in frase:
    frase_modificada = frase.replace(palavra, substituir).upper()
    print(f"Frase modificada: {frase_modificada}")
else:
    print("A palavra fornecida não está na frase.")
