# 10. Crie uma função chamada repetir_palavra que receba uma palavra e um número opcional de vezes (padrão 3).
# A função deve retornar a palavra repetida pelo número de vezes especificado, separadas por espaço.
# Exemplo: repetir_palavra("Oi", 5) retorna "Oi Oi Oi Oi Oi".

def repetir_palavra(palavra,numero=3):
    resp = ""
    for cont in range(numero):
        resp += palavra + " "
    return resp

#Programa Principal
p = str(input("Digite uma palavra: "))
n = input("Digite um número: ")
if n.strip() == "":
    resposta = repetir_palavra(p)
    print(resposta)
else:
    n = int(n)
    resposta = repetir_palavra(p,n)
    print(resposta)


#Concluido
