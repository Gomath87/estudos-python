# -*- coding: utf-8 -*-
lista1 = []
lista2 = []
T = int(input())
primeiro = 0
while True:
    if primeiro == T:
        break
    else:
        lista1.append(primeiro)
    primeiro += 1
cont = 0
while True:
    for num in lista1:
        lista2.append(num)
        cont += 1
        if cont == 1000:
            break
    if cont == 1000:
        break
    else:
        continue
for indice, valor in enumerate(lista2):
    print(f"N[{indice}] = {valor}")


