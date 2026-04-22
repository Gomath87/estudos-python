# -*- coding: utf-8 -*-

num = int(input())
soma = 0
for cont in range (num):
    acao,valor = map(str,input().split())
    valor = int(valor)
    if acao == "G":
        soma -= valor
    else:
        soma += valor

if soma >= 0:
    print("A greve vai parar.")
elif soma < 0:
    print("NAO VAI TER CORTE, VAI TER LUTA!")