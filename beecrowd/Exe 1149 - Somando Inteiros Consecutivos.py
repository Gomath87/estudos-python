# -*- coding: utf-8 -*-
soma = cont = 0
while True:
    a,b = map(int,input().split())
    while a <= 0:
        a = map(int,input())
    while b <= 0:
        a = map(int, input())
    if a and b > 0:
        break
while True:
    if cont <= b:
        soma += a
        cont += 1
        soma += 1
    else:
        break
print(f"{soma}")


