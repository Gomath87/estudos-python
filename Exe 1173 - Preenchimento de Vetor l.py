# -*- coding: utf-8 -*-
lista =[]
primeiro = int(input())
for cont in range(1,11):
    lista.append(primeiro)
    primeiro *= 2
for indice,valor in enumerate(lista):
    print(f"N[{indice}] = {valor}")