# -*- coding: utf-8 -*-

cpf = str(input())

for cont in cpf:
    if cont == "." or cont == "-":
        print()
    else:
        print(int(cont),end="")