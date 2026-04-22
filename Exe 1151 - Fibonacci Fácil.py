# -*- coding: utf-8 -*-

quantidade = int(input())
primeiro = 0
segundo = 1
lista = []
if quantidade == 1:
    print(primeiro)
elif quantidade == 2:
    print(primeiro, segundo)
else:
    print(primeiro, segundo,end=" ")
    cont = 2
    while True:
        terceiro = primeiro + segundo
        if cont == quantidade - 1:
            print(terceiro)
        else:
            print(terceiro, end=" ")
        primeiro = segundo
        segundo = terceiro
        cont += 1
        if cont == quantidade:
            break





