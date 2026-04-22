# 1. Crie uma função chamada saudacao que receba um parâmetro opcional 'nome' e retorne uma mensagem de saudação.
# Exemplo: saudacao("Maria") retorna "Olá, Maria!" e saudacao() retorna "Olá, Amigo!".

def saudacao(a='amigo'):
    a = f"Olá, {a}!"
    return a

#Programa principal
nome = str(input("Nome: "))
if nome.strip() == "":
    resposta = saudacao()
else:
    resposta = saudacao(nome)
print(resposta)