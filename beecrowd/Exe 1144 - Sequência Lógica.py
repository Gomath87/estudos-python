# -*- coding: utf-8 -*-

n = int(input())

for cont in range(1,n+1):
    print(f"{cont} {cont*cont} {cont*cont*cont}")
    print(f"{cont} {cont*cont + 1} {cont*cont*cont + 1}")

