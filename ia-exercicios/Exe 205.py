# 8. Crie uma função que receba uma lista de números e retorne a soma de todos os elementos.
# Use uma variável local dentro da função para armazenar a soma.

def numeros(num):
    soma = 0
    for cont in num:
        soma += cont
    return soma

#Programa Principal
lista = [1,2,3,4,5,10]
resposta = numeros(lista)
print(f"A soma de todos os números da lista é {resposta}")


#Concluido