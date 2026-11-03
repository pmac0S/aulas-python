#ATIVIDADE AULA 17
arquivo = open ("CANIL.txt", "w")
nomes = []
raças = []
for i in range (5):
    nome = input("Digite o nome do animal: ")
    raça = input("Digite a raça do animal: ")
    nomes.append(nome)
    raças.append(raça)
    arquivo.write (nome + " " + raça + "\n")
arquivo.close()




