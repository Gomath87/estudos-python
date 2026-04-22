# -*- coding: utf-8 -*-

while True:
    try:
        num = int(input())
        a = list(map(int,input().split()))

        maior = max(a)

        if maior < 10:
            print(1)
        elif maior >= 10 and maior < 20:
            print(2)
        else:
            print(3)
    except EOFError:
        break
