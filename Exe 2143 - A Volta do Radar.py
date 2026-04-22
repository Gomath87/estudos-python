# -*- coding: utf-8 -*-

while True:
    num = int(input())
    if num == 0:
        break
    else:
        for cont in range(num):
            a = int(input())
            if a % 2 == 0:
                b = a - 2
                c = (b * 2) + 2
                print(c)
            else:
                b = a - 1
                c = (b * 2) + 1
                print(c)