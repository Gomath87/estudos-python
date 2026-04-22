# -*- coding: utf-8 -*-

A, B, C, D = map(int, input().split())
somaCD = C + D
somaAB = A + B
par = 3
if A % 2 == 0:
    par = 0
else:
    par = 1

if B > C and D > A and somaCD > somaAB and C > 0 and D > 0 and par == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")