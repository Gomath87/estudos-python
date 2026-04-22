# -*- coding: utf-8 -*-

N = int(input())
contador = contador2 = soma = 0

while True:
    X, Y = map(int,input().split())
    contador += 1
    while True:
        if X % 2 == 1:
            soma += X
            contador2 +=1
        X += 1
        if contador2 == Y:
            break
    print(soma)
    soma = 0
    contador2 = 0

    if contador == N:
        break
    else:
        continue




