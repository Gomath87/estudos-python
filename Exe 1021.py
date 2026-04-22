# -*- coding: utf-8 -*-

valor = float(input())
centavos = int(round(valor * 100))

cem = cinquenta = vinte = dez = cinco = dois = 0
ummoeda = cinquentacent = vinteecincocent = dezcent = cincocent = umcent = 0


cem = centavos // 10000
centavos %= 10000

cinquenta = centavos // 5000
centavos %= 5000

vinte = centavos // 2000
centavos %= 2000

dez = centavos // 1000
centavos %= 1000

cinco = centavos // 500
centavos %= 500

dois = centavos // 200
centavos %= 200

# Moedas
ummoeda = centavos // 100
centavos %= 100

cinquentacent = centavos // 50
centavos %= 50

vinteecincocent = centavos // 25
centavos %= 25

dezcent = centavos // 10
centavos %= 10

cincocent = centavos // 5
centavos %= 5

umcent = centavos // 1
centavos %= 1

print("NOTAS:")
print(f"{cem} nota(s) de R$ 100.00")
print(f"{cinquenta} nota(s) de R$ 50.00")
print(f"{vinte} nota(s) de R$ 20.00")
print(f"{dez} nota(s) de R$ 10.00")
print(f"{cinco} nota(s) de R$ 5.00")
print(f"{dois} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{ummoeda} moeda(s) de R$ 1.00")
print(f"{cinquentacent} moeda(s) de R$ 0.50")
print(f"{vinteecincocent} moeda(s) de R$ 0.25")
print(f"{dezcent} moeda(s) de R$ 0.10")
print(f"{cincocent} moeda(s) de R$ 0.05")
print(f"{umcent} moeda(s) de R$ 0.01")


