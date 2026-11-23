#atividade da aula 10:
palavras = []
for i in range (5):
    palavras.append(input("Digite uma palavra: "))
    palavras.sort()
    print (f"Suas palavras foram: {palavras}")

# e para colocar essas palavras em ordem alfabética?
# Solucionar um problema como esse pode-ser com uma biblioteca de livros, por os livros em ordem alfabética por exemplo
# para por em ordem alfabética basta só você criar outra função palavras.sort(), só isso, em baixo da função palavras.append()

livros = []
while True:
    livros.append(input("Digite o seu livro: "))
    livros.sort()
    if livros=="sair" or livros=="Sair":
        break
    print(livros)

    # como que eu faço o "sair" em livros?
