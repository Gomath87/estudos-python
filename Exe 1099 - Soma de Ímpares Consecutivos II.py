# -*- coding: utf-8 -*-

N = int(input())
quantidade = 0
somaimpar = 0
while quantidade < N:
    n1 , n2 = map(int,input().split())
    menor = 0
    maior = 0
    if n1 > n2:
        maior = n1
        menor = n2
    else:
        maior = n2
        menor = n1
    for cont in range(menor+1,maior):
        if cont % 2 != 0:
            somaimpar += cont
    print(somaimpar)
    somaimpar = 0
    quantidade += 1

