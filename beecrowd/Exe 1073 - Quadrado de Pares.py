# -*- coding: utf-8 -*-

N = int(input())

for cont in range(1,N+1):
    if cont % 2 == 0:
        print(f"{cont}^2 = {cont**2}")
