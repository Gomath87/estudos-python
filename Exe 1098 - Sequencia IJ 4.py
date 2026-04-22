# -*- coding: utf-8 -*-

I = 0
J = 1
Joriginal = 1
cont = 0
repparaint = 0
while I <= 2:
    if I == int(I):
        print(f"I={int(I)} J={int(J)}")
    else:
        print(f"I={I:.1f} J={J:.1f}")
    cont += 1
    J += 1
    if cont == 3:
        cont = 0
        I = float(f"{I + 0.2:.1f}")
        J = Joriginal + I
        repparaint += 1
        if repparaint == 5:
            repparaint = 0





