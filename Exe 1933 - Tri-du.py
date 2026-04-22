# -*- coding: utf-8 -*-

a,b = map(int,input().split())

if a == b:
    print(a)
else:
    lista = [a,b]
    maior = max(lista)
    print(maior)