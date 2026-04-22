# -*- coding: utf-8 -*-

maior = 0
lista = []
for cont in range (1,101):
    n = int(input())
    lista.append(n)
    if n >= maior:
        maior = n
posicao = lista.index(maior)
print(maior)
print(posicao+1)
