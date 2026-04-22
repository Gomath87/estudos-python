# -*- coding: utf-8 -*-

salario = float(input())

if salario <= 2000.00:
    print("Isento")
elif salario > 2000 and salario <= 3000:
    salario -= 2000
    imposto = salario * (8/100)
    print(f"R$ {imposto:.2f}")
elif salario > 3000 and salario <= 4500:
    imposto = 80.00
    salario -= 3000
    imposto2 = salario * (18/100)
    total = imposto + imposto2
    print(f"R$ {total:.2f}")
elif salario > 4500:
    imposto = 350.00
    salario -= 4500
    imposto2 = salario * (28/100)
    total = imposto + imposto2
    print(f"R$ {total:.2f}")
