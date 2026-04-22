# -*- coding: utf-8 -*-

teste = int(input())
z = 0
boost = 0
a = 0
diferente = 0
igual = 0
secundary = ""
op = ""
while a < teste:
    pessoas = int(input())
    while z < pessoas:
        op = str(input())
        boost += 1
        if boost == 1:
            secundary = op
        else:
            if secundary != op:
                secundary = op
                diferente += 1
            elif secundary == op:
                secundary = op
                igual += 1
        z += 1

    z = 0
    boost = 0
    if igual > 0:
        print(op)
    elif igual == 0:
        print("ingles")
    diferente = 0
    secundary = ""
    igual = 0
    a += 1
    if a == teste:
        break
