#AULA DE ARQUIVO:
arquivo = open ("exemplo.txt", "a")
arquivo.write ("eu quero salvar um arquivo")
arquivo.close()

#DE NOVO:
file = open ("file_example.txt", "w") #tinha esquecido de colocar o .txt
for i in range (5):
    name = input(f"write {i+1} name: ") #tinha esquecido de colocar o {i+1} 
    file.write (name + "\n")
file.close()

#DE NOVO: 
fil = open ("file_example_2.txt", "w")
for i in range (5):
    nome = input(f"write {i+1} name: ")
    sobrenome = input(f"write your {i+1} second name: ")
    fil.write (nome + " " + sobrenome + "\n")
fil.close()

#ESCRITA DE ARQUIVOS:
nomes_completos = [] #criou uma lista, para quando o usuário escrever os nomes, eles são adcionados nessa lista  
for i in range (5):
    nome = input(f"Digite o {i+1} nome: ")
    sobrenome = input(f"Digite o {i+1} sobrenome: ")
    nomes_completos.append(f"{nome} {sobrenome}")
arquivo = open("nomes.txt", "w")
arquivo.writelines("\n".join(nomes_completos) + "\n")
arquivo.close()
                   