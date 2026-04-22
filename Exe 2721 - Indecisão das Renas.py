# -*- coding: utf-8 -*-

lista = list(map(int, input().split()))
bolinhas = sum(lista)
lista = ['Dasher','Dancer','Prancer','Vixen','Comet','Cupid','Donner','Blitzen','Rudolph']
resultado = " "
quantidade = 0
lista2 = []

while quantidade != bolinhas:
    for cont in lista:
        lista2.append(cont)
        quantidade += 1
        if quantidade == bolinhas:
            print(lista2[0])
            break
        else:
            lista2.clear()
            continue