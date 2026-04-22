# -*- coding: utf-8 -*-

bolinhas = int(input())
galhos = int(input())

if galhos % 2 != 0:
    galhos -= 1

calculo = galhos / 2
calculobolinhas = calculo - bolinhas

if calculobolinhas <= 0:
    print("Amelia tem todas bolinhas!")
else:
    print(f"Faltam {calculobolinhas:.0f} bolinha(s)")