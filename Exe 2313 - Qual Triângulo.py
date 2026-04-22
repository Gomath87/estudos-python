# -*- coding: utf-8 -*-

A,B,C = map(int,input().split())
lista = [A,B,C]
meio = 0
maximo = max(lista)
minimo = min(lista)
lista.remove(maximo)
soma = sum(lista)
lista.remove(minimo)

for cont in lista:
    meio = cont


if soma <= maximo:
    print("Invalido")
elif soma > maximo:

    if A == B and A == C:
        resultado = (minimo**2) + (meio**2)
        if resultado == maximo**2:
            print("Valido-Equilatero")
            print("Retangulo: S")
        else:
            print("Valido-Equilatero")
            print("Retangulo: N")

    elif A == B or A == C or B == C:
        resultado = (minimo ** 2) + (meio ** 2)
        if resultado == maximo**2:
            print("Valido-Isoceles")
            print("Retangulo: S")
        else:
            print("Valido-Isoceles")
            print("Retangulo: N")
    else:
        resultado = (minimo ** 2) + (meio ** 2)
        if resultado == maximo ** 2:
            print("Valido-Escaleno")
            print("Retangulo: S")
        else:
            print("Valido-Escaleno")
            print("Retangulo: N")

