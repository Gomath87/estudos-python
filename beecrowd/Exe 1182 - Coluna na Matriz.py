# -*- coding: utf-8 -*-

matriz = []

numerocoluna = int(input())
operacao = str(input())
soma = div = media = 0
for coluna in range(12):
    linha = []
    for linhaa in range(12):
        n = float(input())
        linha.append(n)
    matriz.append(linha)


if operacao == "S":
    for cont in matriz:
        for p,v in enumerate(cont):
            if p == numerocoluna:
                soma += v
    print(f"{soma:.1f}")

elif operacao == "M":
    for cont in matriz:
        for p,v in enumerate(cont):
            if p == numerocoluna:
                soma += v
                div += 1
    media = soma / div
    print(f"{media:.1f}")




