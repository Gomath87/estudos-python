# -*- coding: utf-8 -*-

pulo, quantidadecanos = map(int,input().split())
altura = list(map(int,input().split()))[:quantidadecanos]

lista = []

for posicao in range(len(altura) - 1):
    if altura[posicao] <= altura[posicao + 1]:
        subtracao = altura[posicao + 1] - altura[posicao]
        if subtracao <= pulo:
            lista.append(1)
        else:
            lista.append(0)

    elif altura[posicao] > altura[posicao + 1]:
        subtracao = altura[posicao] - altura[posicao + 1]
        if subtracao <= pulo:
            lista.append(1)
        else:
            lista.append(0)

if 0 in lista:
    print("GAME OVER")
else:
    print("YOU WIN")
