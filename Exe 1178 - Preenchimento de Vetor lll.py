# -*- coding: utf-8 -*-
lista = list()
X = float(input())
lista.append(X)

for cont in range (0,99):
    proximo = lista[cont] /2
    lista.append(proximo)

for indice,valor in enumerate (lista):
    print(f"N[{indice}] = {valor:.4f}")