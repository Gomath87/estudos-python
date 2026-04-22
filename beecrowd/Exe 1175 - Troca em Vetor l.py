# -*- coding: utf-8 -*-
lista = list()
for cont in range(1,21):
    num = int(input())
    lista.append(num)
invertida = list(reversed(lista))
for indice,valor in enumerate(lista):
    print(f"N[{indice}] = {invertida[indice]}")
