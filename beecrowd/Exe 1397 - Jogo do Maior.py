# -*- coding: utf-8 -*-

while True:
    ja = jb = 0
    cont = 0
    c = int(input())
    if c == 0:
        break
    else:
        while True:
            if cont == c:
                break
            else:
                a , b = map(int,input().split())
                if a > b:
                    ja += 1
                elif b > a:
                    jb += 1
            cont += 1
        print(f"{ja} {jb}")


