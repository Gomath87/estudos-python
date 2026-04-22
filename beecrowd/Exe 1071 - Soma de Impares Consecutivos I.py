# -*- coding: utf-8 -*-

X = int(input())
Y = int(input())

menor = min(X, Y)
maior = max(X, Y)

soma = 0
for i in range(menor + 1, maior):
    if i % 2 != 0:
        soma += i

print(soma)


