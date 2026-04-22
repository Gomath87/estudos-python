# -*- coding: utf-8 -*-

soma = flag = resultado = 0

while True:
    try:
        nome = str(input())
        metros = int(input())
        flag += 1
        soma += metros
    except EOFError:
        resultado = soma / flag
        print(f"{resultado:.1f}")
        break

