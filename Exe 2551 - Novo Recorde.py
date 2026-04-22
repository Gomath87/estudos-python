# -*- coding: utf-8 -*-

while True:
    try:
        num = int(input())
        comparacao = 0
        for cont in range (1,num+1):
            minutos, distancia = map(int,input().split())
            if cont == 1:
                comparacao = distancia / minutos
                print(cont)
            else:
                a = distancia / minutos
                if a > comparacao:
                    comparacao = a
                    print(cont)

    except EOFError:
        break