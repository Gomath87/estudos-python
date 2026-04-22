# -*- coding: utf-8 -*-

A, B, C = map(float,input().split())
lista = [A,B,C]
lista.sort(reverse=True)
A = lista[0]
B = lista [1]
C = lista [2]

if A >= B+C:
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    if A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    if A**2 < (B**2 + C**2):
        print("TRIANGULO ACUTANGULO")

    if A == B and A == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")



