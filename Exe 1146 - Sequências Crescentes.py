# -*- coding: utf-8 -*-


while True:
    x = int(input())
    if x > 0:
        for cont in range(1,x+1):
            if cont == x:
                print(cont)
            else:
                print(cont, end=" ")
    else:
        break
