# -*- coding: utf-8 -*-

x = int(input())
while True:
    z = int(input())
    if z > x:
        break
cont = 1
proximonumero = x + cont
soma = x + proximonumero
quantidadedenumeros = 2

while soma < z:
    proximonumero += cont
    soma += proximonumero
    quantidadedenumeros += 1


print(quantidadedenumeros)






