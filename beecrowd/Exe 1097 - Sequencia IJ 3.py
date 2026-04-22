# -*- coding: utf-8 -*-

I = 1
J = 7
cont = 0
while I <= 9:
    print(f"I={I} J={J}")
    cont += 1
    J -= 1
    if cont == 3:
        cont = 0
        I += 2
        J += 5

