# -*- coding: utf-8 -*-

frango, bife, massa = map(int,input().split())
pedidosF,pedidosB,pedidosM = map(int,input().split())

resultfrango = frango - pedidosF
resultbife = bife - pedidosB
resultmassa = massa - pedidosM

lista = []

lista.append(resultfrango)
lista.append(resultbife)
lista.append(resultmassa)
soma = 0

for cont in lista:
    if cont < 0:
        soma += abs(cont)

print(soma)


