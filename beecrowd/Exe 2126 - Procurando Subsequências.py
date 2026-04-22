# -*- coding: utf-8 -*-
caso = 1
while True:
    try:
        n1 = int(input())
        n2 = int(input())
        n1 = str(n1)          #Transforma em str para poder usar o count
        n2 = str(n2)          #Transforma em str para poder usar o count

        n3 = n2.count(n1)     #Vê quantas vezes se repete a sequencia de n1 em n2
        if n3 == 1:
            n4 = (n2.find(n1))+1
            print(f"Caso #{caso}:")
            print(f"Qtd.Subsequencias: {n3}")
            print(f"Pos: {n4}")
        elif n3 > 1:
            n4 = (n2.rfind(n1))+1
            print(f"Caso #{caso}:")
            print(f"Qtd.Subsequencias: {n3}")
            print(f"Pos: {n4}")
        elif n3 == 0:
            print(f"Caso #{caso}:")
            print("Nao existe subsequencia")
        caso += 1
        print()

    except EOFError:
        break