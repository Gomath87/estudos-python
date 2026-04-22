# -*- coding: utf-8 -*-

while True:
    m, n = map(int, input().split())

    if m <= 0 or n <= 0:
        break
    soma = 0
    numeros_sequencia = []

    if m > n:
        menor = n
        maior = m
    else:
        menor = m
        maior = n

    for cont in range(menor, maior + 1):
        soma += cont
        numeros_sequencia.append(str(cont))
    print(" ".join(numeros_sequencia) + f" Sum={soma}")
