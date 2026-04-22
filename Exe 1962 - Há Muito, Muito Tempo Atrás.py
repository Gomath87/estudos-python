# -*- coding: utf-8 -*-

n = int(input())
anoatual = 2015

for cont in range(1,n+1):
    t = int(input())
    calculo = anoatual - t
    if calculo <= 0:
        resultado = abs(calculo)+1
        print(f"{resultado} A.C")
    else:
        resultado = calculo
        print(f"{resultado} D.C")