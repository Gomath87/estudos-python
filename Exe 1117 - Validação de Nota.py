# -*- coding: utf-8 -*-

media = cont = somanota = 0
while True:
    nota = float(input())
    if nota > -1 and nota < 10.1:
        somanota += nota
        cont +=1
        if cont == 2:
            break
    else:
        print("nota invalida")
media = somanota / cont
print(f"media = {media:.2f}")


