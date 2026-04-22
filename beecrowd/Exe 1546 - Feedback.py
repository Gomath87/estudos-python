# -*- coding: utf-8 -*-

quantC = int(input())
a = 0
b = 0
while True:
    if b == quantC:
        break
    else:
        c = int(input())
        while a != c:
            test = int(input())
            if test == 1:
                print("Rolien")
            elif test == 2:
                print("Naej")
            elif test == 3:
                print("Elehcim")
            elif test == 4:
                print("Odranoel")
            a += 1
    a = 0
    b += 1



