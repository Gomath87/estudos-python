# -*- coding: utf-8 -*-

while True:
    try:
        num = int(input())
        if num >= 0 and num < 90:
            print("Bom Dia!!")
        elif num >= 90 and num < 180:
            print("Boa Tarde!!")
        elif num >= 180 and num < 270:
            print("Boa Noite!!")
        elif num >= 270 and num < 360:
            print("De Madrugada!!")
        elif num == 360:
            print("Bom Dia!!")
    except EOFError:
        break