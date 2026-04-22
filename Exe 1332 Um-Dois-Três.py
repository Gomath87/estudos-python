

a = int(input())
conta = 1
contador = 0
um = "one"
dois = "two"
Num = 0
Ndois = 0
while conta <= a:
    numero = str(input()).lower()
    if len(numero) == 3:
        for cont in numero:
            if cont == um[contador]:
                Num += 1
            if cont == dois[contador]:
                Ndois += 1
            contador += 1

        if Num > Ndois:
            print("1")
        else:
            print("2")


    elif len(numero) > 3:
        print("3")

    conta += 1
    contador = 0
    Num = 0
    Ndois = 0