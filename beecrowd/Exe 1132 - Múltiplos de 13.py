# -*- coding: utf-8 -*-

X = int(input())
Y = int(input())
C = 0
Soma = 0
if X > Y:
   C = X
   X = Y
   Y = C

for cont in range(X,Y+1)
    if cont % 13 != 0:
        Soma += cont
print(Soma)