# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
# o usuário digitar o valor 000, que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag).
ndigitados = 0
soma = 0
n = int
while n != 000:
    n = int(input("Digite um número: "))
    ndigitados += 1
    soma += n
    if n == 000: #condição para excluir o número "000" que é a flag para parar o programa. Subtraindo 1 para retirar a soma do "000".
        ndigitados += -1
print(f"Foram digitados {ndigitados} números")
print(f"E a soma deles é {soma}")
