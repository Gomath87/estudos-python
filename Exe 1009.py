# -*- coding: utf-8 -*-

nome = str(input())
salfixo = float(input())
totvendas = float(input())

comissao = totvendas * (15/100)
total = salfixo + comissao
print(f"TOTAL = R$ {total:.2f}")



