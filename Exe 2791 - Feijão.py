# -*- coding: utf-8 -*-

cum,cdois,ctres,cquatro = map(int,input().split())
lista = []
lista.append(cum)
lista.append(cdois)
lista.append(ctres)
lista.append(cquatro)
for indice, valor in enumerate(lista):
    if valor == 1:
        posicao = indice +1
        print(posicao)
