# -*- coding: utf-8 -*-

num = int(input())
entrada = input()
lista = list(map(int, entrada.split()))
a = 0
b = 1
for posicao,valor in enumerate(lista):
    if posicao == 0:
        continue
    else:
        if valor < lista[a]:
            pos = posicao
            b = 10
            break
        elif valor >= lista[a]:
            b = 0
            a += 1
if b == 0:
    print(b)
elif b == 10:
    print(pos+1)
