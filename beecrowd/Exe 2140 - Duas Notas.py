# -*- coding: utf-8 -*-

while True:
    a, b = map(int,input().split())
    dinheiro = b - a
    contnotas = 0

    if a == 0 and b == 0:
        break

    if dinheiro == 100:
        print("possible")

    elif dinheiro == 50:
        print("impossible")

    elif dinheiro == 20:
        print("possible")

    elif dinheiro == 10:
        print("possible")
    elif dinheiro == 5:
        print("impossible")
    else:
        while True:
            if dinheiro > 100:
                div100 = dinheiro // 100
                dinheiro = dinheiro % 100
                contnotas += div100


            elif dinheiro > 50:
                div50 = dinheiro // 50
                dinheiro = dinheiro % 50
                contnotas += div50

            elif dinheiro > 20:
                div20 = dinheiro // 20
                dinheiro = dinheiro % 20
                contnotas += div20

            elif dinheiro > 10:
                div10 = dinheiro // 10
                dinheiro = dinheiro % 10
                contnotas += div10

            elif dinheiro > 5:
                div5 = dinheiro // 5
                dinheiro = dinheiro % 5
                contnotas += div5

            elif dinheiro > 2:
                div2 = dinheiro // 2
                dinheiro = dinheiro % 2
                contnotas += div2

            if dinheiro < 2:
                break

        if contnotas > 2:
            print("impossible")
        elif contnotas < 2:
            print("impossible")
        elif contnotas == 2:
            print("possible")

