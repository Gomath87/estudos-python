# 6. Crie uma função que receba um número e retorne True se for par e False se for ímpar.
# Adicione uma docstring explicando o que a função faz.

def parouimpar(a):
    if a % 2 == 0:
        return "True"
    else:
        return "False"

#Programa principal
b = int(input("Digite um número para saber se o mesmo é ou não par: "))
resposta = parouimpar(b)
print(resposta)





#Concluido