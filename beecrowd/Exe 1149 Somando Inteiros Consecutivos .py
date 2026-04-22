# -*- coding: utf-8 -*-

valores = list(map(int,input().split()))

A = valores[0]

for cont in valores[1:]:
    if cont > 0:
        N = cont
        break
cont = 1
soma = A

while cont != N:
    soma += A+cont
    cont += 1

print(soma)



