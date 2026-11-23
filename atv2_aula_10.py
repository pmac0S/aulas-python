# Atividade 2 da aula 10:
reptil=[]
mamifero=[]
ave=[]
outro=[]
for i in range (1, 11):
    nome = input(f"Digite o nome do {i} animal: ")

    print("Em qual categoria deseja cadastra-lo?")
    print("1-Réptil")
    print("2-mamífero")
    print("3-ave")
    print("4-outro")

    categoria = int(input("Digite o número da categoria: "))

    if categoria == 1:
        reptil.append(nome)
    elif categoria == 2:
        mamifero.append(nome)
    elif categoria == 3:
        ave.append(nome)
    elif categoria == 4:
        outro.append(nome)
    else:
        print("Númeor inválido!")

    reptil.sort()
    mamifero.sort()
    ave.sort()
    outro.sort()

print("\n=== LISTA DE ANIMAIS ===")
print(f"Répteis:{reptil}, quantidade: {len(reptil)}")
print(f"Mamíferos:{mamifero}, quantidade: {len(mamifero)}")
print(f"Aves:{ave}, quantidade: {len(ave)}")
print(f"Outro:{outro}, quantidade: {len(outro)}")

# como vê a quantidade? len
# a forma que você escreveu o len está errada, não se coloca a lista.len()
# para usar o len voce deve colocar o len(lista)
