# -*- coding: utf-8 -*-

frase = str(input())
a = b = ""

for posicao,valor in enumerate(frase):
    if valor == ",":
        a = frase[0:posicao]
        b = frase[posicao+1:]

print(a)
print(b)
