# -*- coding: utf-8 -*-

while True:
    try:
        s = str(input())
        a = int(input())
        numeros = list(map(int, input().split()))
        soma = ""
        for cont in numeros:
            soma += s[cont-1]
        print(soma)
    except EOFError:
        break