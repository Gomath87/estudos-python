# -*- coding: utf-8 -*-

numero = int(input())

for cont in range(1,numero+1):   # Laço de repetição que vai de 1 até o número digitado
    if cont % 2 != 0:            # Verifica se o número é ímpar (resto da divisão por 2 é diferente de 0)
        print(cont)


