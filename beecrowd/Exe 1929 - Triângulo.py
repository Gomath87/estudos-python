# -*- coding: utf-8 -*-

A,B,C,D = map(int,input().split())
lista = [[A,B,C],[A,B,D],[A,C,D],[B,C,D]]
forma = 0
for posicao,valor in enumerate(lista):
    maximo = max(valor)
    indice = valor.index(maximo)
    listatemporaria = []
    for cont in valor:
        if cont != valor[indice]:
            listatemporaria.append(cont)
            if sum(listatemporaria) > maximo:
                forma += 1
                listatemporaria.clear()
if forma >= 1:
    print("S")
else:
    print("N")









