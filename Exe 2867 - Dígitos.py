# -*- coding: utf-8 -*-

n = int(input())
for cont in range(n):
    num, pot = map(int,input().split())
    a = num ** pot
    print(f"{len(str(a))}")