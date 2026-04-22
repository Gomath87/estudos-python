# -*- coding: utf-8 -*-

hora = str(input())
listahora = list(hora)

h = int(listahora[0])
min1 = int(listahora[2]) * 10
min2 = int(listahora[3])
somamin = (h*60) + min1 + min2

if somamin <= 420:
    print("Atraso maximo: 0")
else:
    resultado = (somamin + 60) - 480
    print(f"Atraso maximo: {resultado}")

