# -*- coding: utf-8 -*-

inicio , encontradas , vazias = map(int,input().split())
dgarrafa = (inicio + encontradas) / vazias
r = (inicio + encontradas) % vazias

soma = dgarrafa + r     #Aqui recebe a divisão e o resto da divisão, resultado no total das garrafas
tot = dgarrafa
if soma >= vazias:
    while True:
        dgarrafa = soma / vazias
        r = soma % vazias
        tot += dgarrafa
        soma = dgarrafa + r
        if soma >= vazias:
            continue
        else:
            print(tot)
            break

else:
    print(soma)

