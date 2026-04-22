# -*- coding: utf-8 -*-

while True:
    try:
        visitantes,a_minima,a_maxima = map(int,input().split())
        resp = 0
        for cont in range(visitantes):
            num = int(input())
            if num >= a_minima and num <= a_maxima:
                resp += 1
        print(resp)

    except EOFError:
        break