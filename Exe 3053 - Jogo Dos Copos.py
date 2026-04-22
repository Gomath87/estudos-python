# -*- coding: utf-8 -*-

num = int(input())
moeda = str(input())
A = B = C = 0
if moeda == "A":
    A = 1
    B = 0
    C = 0
elif moeda == "B":
    A = 0
    B = 1
    C = 0
elif moeda == "C":
    A = 0
    B = 0
    C = 1

momen = 0

for cont in range(num):
    mov = int(input())
    if mov == 1:
        momen = A
        A = B
        B = momen
        momen = 0
    elif mov == 2:
        momen = B
        B = C
        C = momen
        momen = 0
    elif mov == 3:
        momen = A
        A = C
        C = momen
        momen = 0

lista = [A, B, C]
aqui = 0

for posicao, valor in enumerate(lista):
    if valor == 1:
        aqui = posicao
if aqui == 0:
    print("A")
elif aqui == 1:
    print("B")
elif aqui == 2:
    print("C")