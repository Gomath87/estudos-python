# -*- coding: utf-8 -*-

while True:
    try:
        N, Q = map(int,input().split())
        lista = []
        for cont in range(N):
            num = int(input())
            lista.append(num)

        crescente = sorted(lista, reverse=True)

        for cont in range(Q):
            num = int(input())
            print(crescente[num - 1])

    except EOFError:
        break