# -*- coding: utf-8 -*-

num = int(input())

for cont in range(num):
    entrada = list(map(int, input().split()))
    entrada.pop(0)
    soma = 0
    for cont2 in entrada:
        soma += cont2 -1
    print(f"{soma + 1}")