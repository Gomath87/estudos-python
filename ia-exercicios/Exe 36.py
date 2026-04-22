#1. Crie uma tupla com 4 números inteiros e mostre:
#Todos os valores
#O maior e o menor valor
#A soma dos valores

numeros = (1,7,12,5)

print(f"Todos os valores são: {numeros}")
print(f"Maior número {max(numeros)} e menor número {min(numeros)}")
cont = 0
soma = 0
while cont < 4:
    soma =  soma + numeros[cont]
    cont += 1
print(f"A soma dos valores dentro da tupla é {soma}")