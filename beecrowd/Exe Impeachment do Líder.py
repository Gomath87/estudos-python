# -*- coding: utf-8 -*-

while True:
    try:
        n = int(input())
        numeros = list(map(int,input().split()))
        um = numeros.count(1)
        porcentagem = n / 3
        porcentagem *= 2
        if um >= porcentagem:
            print("impeachment")
        else:
            print("acusacao arquivada")
        numeros.clear()

    except EOFError:
        break