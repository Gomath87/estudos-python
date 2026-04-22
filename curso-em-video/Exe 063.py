# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros
# elementos de uma Sequência de Fibonacci.
#Ex:
# 0 -- 1 -- 1 -- 2 -- 3 -- 5 -- 8
n = int(input("Quantos elementos deseja ver da sequencia de fibonacci? "))
primeiro = 0
segundo = 1
contador = 3
if n == 1:
    print("0")
elif n == 2:
    print("0 -- 1")
else:
    print(primeiro,"--",segundo,"--",end="")
    while contador <= n:
        proximonumero = primeiro + segundo
        print(proximonumero,"--",end="")
        primeiro = segundo
        segundo = proximonumero
        contador += 1

print(f"\nEsses foram os primeiro {n} elementos da sequencia de fibonacci")



