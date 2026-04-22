# -*- coding: utf-8 -*-



cifra, frases = map(int, input().split())
t1 = str(input())
t2 = str(input())
dicionario = {}

for cont in range(cifra):
    dicionario[t1[cont]] = t2[cont]

for cont in range(frases):
    msg = str(input())
    msg2 = msg.upper()
    novamsg = ""

    # Aqui para decifrar
    for cont2 in msg2:
        trocou = False
        for chave, valor in dicionario.items():
            if cont2 == chave:
                novamsg += valor.upper()
                trocou = True
                break

            elif cont2 == valor:
                novamsg += chave
                trocou = True
                break
        if not trocou:
            novamsg += cont2

    # Loop para deixar a saída igual a entrada em questão de maiúsculo e minúsculo
    pos = 0
    essa = ""
    for cont3 in msg:
        if cont3.isupper():
            essa += novamsg[pos].upper()
        elif cont3.islower():
            essa += novamsg[pos].lower()
        else:
            essa += novamsg[pos]
        pos += 1

    print(essa)
print()
