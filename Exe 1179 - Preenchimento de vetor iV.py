# -*- coding: utf-8 -*-
listapar = []
listaimpar = []
for cont in range (1,16):
    num = int(input())
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    if len(listaimpar) == 5:
        for indice,valor in enumerate (listaimpar):
            print(f"impar[{indice}] = {valor}")
        listaimpar.clear()
    if len(listapar) == 5:
        for indice,valor in enumerate(listapar):
            print(f"par[{indice}] = {valor}")
        listapar.clear()

for indice,valor in enumerate (listaimpar):
    print(f"impar[{indice}] = {valor}")

for indice, valor in enumerate(listapar):
    print(f"par[{indice}] = {valor}")


