# -*- coding: utf-8 -*-

dicionario = {'1001': 1.50,
              '1002': 2.50,
              '1003': 3.50,
              '1004': 4.50,
              '1005': 5.50}

unidades = int(input())
soma = 0

for cont in range(unidades):
    a, b = map(str, input().split())
    produto = dicionario[a]
    quantidade = int(b)
    soma += produto * quantidade

print(f"{soma:.2f}")