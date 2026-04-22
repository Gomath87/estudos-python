# -*- coding: utf-8 -*-

while True:
    try:
        a = int(input())
        cont = 0
        b = a
        if a == 1:
            print("0")
        elif a == 2:
            print("1")
        else:
            while True:
                b = b / 2
                cont += 1
                if b == 1:
                    break
            print(cont)

    except EOFError:
        break