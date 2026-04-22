# -*- coding: utf-8 -*-

repeticao = int(input())
primo = 0
for cont in range(1,repeticao+1):
    primo = 0
    numero = int(input())
    for cont in range(2,numero):
        if numero % cont == 0:
            primo +=1
    if primo >= 1:
        print(f"{numero} nao eh primo")
    else:
        print(f"{numero} eh primo")



