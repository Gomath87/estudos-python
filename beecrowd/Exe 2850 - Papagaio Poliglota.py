# -*- coding: utf-8 -*-

while True:
    try:
        a = str(input())
        dicionario = {"esquerda":"ingles","direita":"frances","nenhuma":"portugues","as duas":"caiu"}
        print(dicionario[a])
    except EOFError:
        break