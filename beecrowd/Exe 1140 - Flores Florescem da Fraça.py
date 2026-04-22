# -*- coding: utf-8 -*-

while True:
    a = str(input()).upper()
    lista = a.split()
    if a == "*":
        break
    else:
        palavra = lista[0][0]
        n = 0
        for cont in lista:
            if cont[0] != palavra:
                n += 1
        if n > 0:
            print("N")
        else:
            print("Y")
