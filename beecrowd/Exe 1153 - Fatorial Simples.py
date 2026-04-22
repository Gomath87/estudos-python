# -*- coding: utf-8 -*-

N = int(input())
if N == 0:
    print("1")
else:
    fatorial = N
    for cont in range(N-1,1,-1):
        fatorial *= cont
print(fatorial)
