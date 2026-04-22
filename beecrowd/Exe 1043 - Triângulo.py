# -*- coding: utf-8 -*-

A, B, C = map(float,input().split())
menor1 = 0
menor2 = 0
maior = 0
if A >= B and A >= C:
    maior = A
    menor1 = B
    menor2 = C
elif B >= A and B >= C:
    maior = B
    menor1 = A
    menor2 = C
elif C >= A and C >= B:
    maior = C
    menor1 = A
    menor2 = B
else:
    maior = C
    menor1 = A
    menor2 = B
soma = menor1 + menor2
area = 0
if menor1 + menor2 > maior:
    perimetro = A + B + C
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = ((A + B) * C) / 2
    print(f"Area = {area:.1f}")


