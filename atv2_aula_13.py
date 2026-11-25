# imprimir uma palavra na vertical:
palavra = input("Digite uma palvra: ").upper()
for i in range (len(palavra)):
    print(palavra[:i+1])
