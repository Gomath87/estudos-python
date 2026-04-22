# -*- coding: utf-8 -*-

numero = int(input())
cont = 0
while cont <= 5:
    if numero % 2 != 0:
        print(numero)
        numero += 1
        cont += 1
    else:
        numero += 1
