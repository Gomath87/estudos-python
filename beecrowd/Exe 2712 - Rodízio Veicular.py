# -*- coding: utf-8 -*-

rep = int(input())

for cont in range(rep):
    placa = str(input())
    ultimo = placa[-1]

    if len(placa) > 8 or len(placa) < 8:
        print("FAILURE")
    elif not placa[:3].isupper():
        print("FAILURE")
    elif not placa[:3].isalpha():
        print("FAILURE")
    elif not placa[4:].isnumeric():
        print("FAILURE")
    elif placa[3] != "-":
        print("FAILURE")
    else:
        if ultimo == "1" or ultimo == "2":
            print("MONDAY")
        elif ultimo == "3" or ultimo == "4":
            print("TUESDAY")
        elif ultimo == "5" or ultimo == "6":
            print("WEDNESDAY")
        elif ultimo == "7" or ultimo == "8":
            print("THURSDAY")
        elif ultimo == "9" or ultimo == "0":
            print("FRIDAY")