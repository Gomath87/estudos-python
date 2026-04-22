# -*- coding: utf-8 -*-
ano = mes = dia = 0
idadeemdias = int(input())


while True:
    if idadeemdias >= 365:
        idadeemdias -= 365
        ano += 1
    else:
        break

while True:
    if idadeemdias >= 30:
        idadeemdias -= 30
        mes += 1
    else:
        break

while True:
    if idadeemdias >= 1:
        idadeemdias -= 1
        dia += 1
    else:
        break

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")
