# -*- coding: utf-8 -*-
lista = []
for cont in range (1,101):
    num = float(input())
    lista.append(num)
for indice,valor in enumerate(lista):
    if valor <= 10:
        print(f"A[{indice}] = {valor}")

