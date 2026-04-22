# 1. Contar de 1 até N
#Peça um número N ao usuário e conte de 1 até N.

numero = int(input("Digite um número: "))
if numero == 0:
    print("O número digitado é '0'")
elif numero < 0:
    print("O número digitado é um número negativo")
for cont in range(1,numero + 1):
    print(cont,end=" ")

