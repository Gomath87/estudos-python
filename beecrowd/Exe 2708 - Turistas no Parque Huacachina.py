# -*- coding: utf-8 -*-
jeep = pessoas = 0
while True:
    palavra = input().split()
    if palavra[0] == "ABEND":
        break
    else:
        numero = int(palavra[1])
        palavra = palavra[0]
        if palavra == "SALIDA":
            pessoas += numero
            jeep += 1
        elif palavra == "VUELTA":
            pessoas -= numero
            jeep -= 1

print(pessoas)
print(jeep)
