# -*- coding: utf-8 -*-

n = int(input())

for cont in range (n):
    h,d,g = map(int,input().split())
    if h >= 200 and h <= 300 and d >= 50 and g >= 150:
        print("Sim")
    else:
        print("Nao")

