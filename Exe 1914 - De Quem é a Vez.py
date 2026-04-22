# -*- coding: utf-8 -*-

quantidade = int(input())
for cont in range(1,quantidade+1):
    a = str(input())
    lista = a.split()

    primeira, segunda = map(int, input().split())
    soma = primeira + segunda

    if soma % 2 == 0:
        resultado = "PAR"
    else:
        resultado = "IMPAR"

    if resultado == lista[1]:
        print(lista[0])
    elif resultado == lista[3]:
        print(lista[2])
    lista.clear()