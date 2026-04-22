# -*- coding: utf-8 -*-

gasolina = alcool = diesel = 0
while True:
    n = int(input())
    if n < 1 or n > 4:
        while True:
            n = int(input())
            if n > 0 and n < 5:
                break
    if n == 1:
        alcool += 1
    elif n == 2:
        gasolina += 1
    elif n == 3:
        diesel += 1
    else:
        break
print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")





