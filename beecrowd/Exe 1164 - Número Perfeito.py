# -*- coding: utf-8 -*-

quantidade = int(input())
soma = 0
for cont in range( 1,quantidade+1):
    num = int(input())
    if num == 0:
        print(f"{num} nao eh perfeito")
    else:
        for divisor in range (1,num):
            if num % divisor == 0:
                soma = soma + divisor
        if soma == num:
            print(f"{num} eh perfeito")
        else:
            print(f"{num} nao eh perfeito")
        soma = 0



