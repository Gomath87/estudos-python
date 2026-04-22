# -*- coding: utf-8 -*-

reps = int(input())
dados = dict()
for cont in range(reps):
    nome = str(input())
    pesoNota = float(input())
    n1,n2,n3,n4,n5,n6,n7 = map(float,input().split())
    lista = [n1,n2,n3,n4,n5,n6,n7]
    lista.remove(max(lista))
    lista.remove(min(lista))
    calculo = sum(lista) * pesoNota

    dados[nome] = calculo
    lista.clear()

for chave,valor in dados.items():
    print(f"{chave} {valor:.2f}")

