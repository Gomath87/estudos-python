# -*- coding: utf-8 -*-

n = int(input())

for div in range(0,n):
    x, y = map (int,input().split())
    if y == 0:
        print("divisao impossivel")
    else:
        d = x / y
        print(f"{d:.1f}")


