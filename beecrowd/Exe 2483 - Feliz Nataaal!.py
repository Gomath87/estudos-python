# -*- coding: utf-8 -*-

indice = int(input())
m = "a"
frase = "Feliz nat"
if indice == 0:
    print("Feliz natal!")
else:
    m *= indice
    soma = (frase + m) + "l!"
    print(soma)
