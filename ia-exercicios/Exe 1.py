#🔢 1. Número Par ou Ímpar
#Peça um número inteiro ao usuário e diga se ele é par ou ímpar.

n = int(input("Digite um número inteiro: "))

if n % 2 == 0:
    print(f"O número {n} é PAR!")
else:
    print(f"O número {n} é ÍMPAR!")