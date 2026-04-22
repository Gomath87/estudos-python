contador = contador2 = soma = 0
while True:
    X = int(input())
    if X == 0:
        break
    else:
        while True:
            if X % 2 == 0:
                soma += X
                contador2 += 1
            X += 1
            if contador2 == 5:
                break
        print(soma)
        soma = 0
        contador2 = 0
