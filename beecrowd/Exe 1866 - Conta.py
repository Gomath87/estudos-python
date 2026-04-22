# -*- coding: utf-8 -*-

quantidade = int(input())

for cont1 in range (1,quantidade+1):
    num = int(input())
    somador = 1

    if num == 1:
        print(somador)
    elif num == 0:
        print("0")
    elif num > 1:
        for cont in range(1, num):
            if somador == 1:
                somador -= 1
            elif somador == 0:
                somador += 1
        print(somador)


