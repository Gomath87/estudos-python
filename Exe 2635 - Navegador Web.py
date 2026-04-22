# -*- coding: utf-8 -*-

palavrasPesquisadasm = int(input())
lista = []

for cont in range(palavrasPesquisadasm):
    palavra = str(input())
    lista.append(palavra)
consultas = int(input())

for cont in range(consultas):
    palavra = str(input())
    lista2 = []
    quantidade = 0

    for cont3 in lista:
        if cont3.startswith(palavra):
            quantidade += 1
            lista2.append(cont3)

    if quantidade > 0:
        maximo = len(max(lista2))
        print(f"{quantidade} {maximo}")
    else:
        print("-1")
