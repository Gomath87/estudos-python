# -*- coding: utf-8 -*-

A, B, C = map(int,input().split())

maior = 0
domeio = 0
menor = 0
um = A
dois = B
tres = C

if A >= B and A >= C:
    maior = A
    if B >= C:
        menor = C
        domeio = B
    elif C >= B:
        menor = B
        domeio = C



elif B >= A and B >= C:
    maior = B
    if A >= C:
        menor = C
        domeio = A
    elif C >= A:
        menor = A
        domeio = C

elif C >= A and C >= B:
    maior = C
    if A >= B:
        menor = B
        domeio = A
    elif B >= A:
        menor = A
        domeio = B
elif A == B and A == C:
    maior = A
    domeior = B
    menor = C

print(menor)
print(domeio)
print(maior)
print()
print(um)
print(dois)
print(tres)

