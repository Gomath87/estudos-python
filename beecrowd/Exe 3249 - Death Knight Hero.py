# -*- coding: utf-8 -*-

num = int(input())
soma = 0
for cont in range(num):
    a = str(input())
    if "CD" in a:
        soma += 0
    else:
        soma += 1
print(soma)