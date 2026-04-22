# -*- coding: utf-8 -*-

quantidade = int(input())

for cont in range (1,quantidade+1):
    dicionario = {}
    nome, p = map(str,input().split())
    newton = int(p)
    dicionario["nome"] = nome
    dicionario["newton"] = p

    if dicionario['nome'] == "Thor":
        print("Y")
    else:
        print("N")