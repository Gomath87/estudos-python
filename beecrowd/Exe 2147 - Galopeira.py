# -*- coding: utf-8 -*-

n = int(input())
for cont in range(n):
    galo = str(input())
    seconds = len(galo) / 100
    print(f"{seconds:.2f}")


