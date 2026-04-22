# -*- coding: utf-8 -*-
lista = list()

for cont in range (1,11):
    num = int(input())
    if num <= 0:
        lista.append(1)
    else:
        lista.append(num)

for indice,valor in enumerate(lista):
    print(f"X[{indice}] = {valor}")