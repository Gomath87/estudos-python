# -*- coding: utf-8 -*-

media = cont = somanota = resposta = 0

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

media = cont = somanota = resposta = 0

while True:
    print("novo calculo (1-sim 2-nao)")
    resposta = int(input())
    if resposta == 1:
        somanota = cont = 0
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
    elif resposta == 2:
        break
    else:
        continue



