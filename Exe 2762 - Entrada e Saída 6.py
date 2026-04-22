# -*- coding: utf-8 -*-

num = (input())
flag = 0
for posicao, valor in enumerate(num):
    if valor == ".":
        flag = posicao

a = num[0:flag]
b = num[flag+1 : ]
print(f"{int(b)}.{int(a)}")

