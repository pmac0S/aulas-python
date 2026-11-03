#atividade 2 da aula 8: acumulador
pontuacao = 0
acertos = 0
erros = 0
for i in range (10):
    resposta = (input(f"Questão {i} - o candidato acertou(sim) ou errou(não)? ")) #usar o {i} você não precisa escrever a questão manualmente, o python entende que é a questão 1,2,3,4,5,6,7,8,9,10
    if resposta == "sim":
        acertos += 1
        pontuacao += 0.5
    elif resposta == "não" or resposta == "nao":
        erros += 1
    else:
        print ("resposta inválida!")
        break
print (f"A pontuação do candidato foi: {pontuacao:.2f}")
print (f"A quantidade de acertos foi de: {acertos}")
print (f"Aquantidade de erros foi de: {erros}")

#NESSA QUESTÃO VOCÊ APRENDEU A USAR O ACUMULADOR E O CONTADOR
# APRENDEU A USAR O {I} PARA MOSTRAR A ESTRUTURA DE REPETIÇÃO AUTOMATICAMENTE, SEM PRECISAR ESCREVER ELA MANUALMENTE.