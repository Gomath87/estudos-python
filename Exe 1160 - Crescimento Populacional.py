# -*- coding: utf-8 -*-

quantidades = int(input())

for cont in range (1,quantidades+1):
    City1, City2, P1, P2 = input().split()
    cidade1 = int(City1)
    cidade2 = int(City2)
    P1 = float(P1)
    P2 = float(P2)
    anos = 0
    while True:
        if anos > 100:
            print("Mais de 1 seculo.")
            break
        elif cidade1 <= cidade2:
            cidade1 += int(cidade1 * (P1 / 100))   #Aqui calcula o crescimento por ano da cidade 1
            cidade2 += int(cidade2 * (P2 / 100))  #Aqui calcula o crescimento por ano da cidade 2
            anos += 1
        else:
            print(f"{anos} anos.")
            break





