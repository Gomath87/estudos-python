# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex:
# 5! = 5x4x3x2x1 + 120

n = int(input("Digite um número para saber seu respectivo fatorial: "))
contador = n
fatorial = 1

while contador > 0:
    fatorial = fatorial * contador
    contador = contador - 1
print(f"O fatorial de {n} é igual a {fatorial}")







