# -*- coding: utf-8 -*-
X,Y = map(int,input().split())
pos = 0
for cont in range(1,Y+1):
    pos += 1
    if pos <= X-1:
        print(cont, end=" ")

    elif pos == X:
        print(cont)
        pos = 0

