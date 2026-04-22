# -*- coding: utf-8 -*-

par = 0
for cont in range (5):          # Laço para ler 5 números
    numero = int(input())
    if numero % 2 == 0:         # Verifica se o número é par (ou seja, resto da divisão por 2 é zero)
        par += 1                # Incrementa o contador de pares
print(f"{par} valores pares")