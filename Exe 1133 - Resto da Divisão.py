# -*- coding: utf-8 -*-

X = int(input())
Y = int(input())
if X < Y:
    for cont in range(X+1,Y):
        if cont % 5 == 2 or cont % 5 == 3:
            print(cont)
elif Y < X:
    for cont in range(Y+1,X):
        if cont % 5 == 2 or cont % 5 == 3:
            print(cont)
