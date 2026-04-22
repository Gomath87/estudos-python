# -*- coding: utf-8 -*-

lista = []
try:
    while True:
        linha = str(input())
        if linha not in lista:
            lista.append(linha)
except EOFError:
    pass

print(len(lista))