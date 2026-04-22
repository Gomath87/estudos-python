# -*- coding: utf-8 -*-

numero = int(input())
p = 0
for cont in range(numero):
    num = str(input())
    if num == "P=NP":
        print("skipped")
    else:
        for posicao,valor in enumerate(num):
            if valor == "+":
                p = posicao
        a = (num[:p])
        b = (num[p+1:])
        soma = int(a) + int(b)
        print(soma)

