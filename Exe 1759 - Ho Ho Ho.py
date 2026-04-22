# -*- coding: utf-8 -*-

num = int(input())
a = "Ho"
lista = []
for cont in range(num):
    lista.append(a)

for pos,val in enumerate(lista):
    if pos == num-1:
        print(f"{val}!")
    else:
        print(f"{val} ",end="")