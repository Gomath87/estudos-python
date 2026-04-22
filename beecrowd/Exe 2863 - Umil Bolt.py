# -*- coding: utf-8 -*-

while True:
    try:
        n = int(input())
        lista = []
        for cont in range(n):
            num = float(input())
            lista.append(num)
        melhorTempo = min(lista)
        print(melhorTempo)
    except EOFError:
        break