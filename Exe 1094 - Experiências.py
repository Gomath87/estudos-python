# -*- coding: utf-8 -*-

N = int(input())
somaC = 0
somaR = 0
somaS = 0
for cont in range (N):
    a = str(input())
    if "C" in a:
        inteiroC = int(a.split()[0])
        somaC += inteiroC
    elif "R" in a:
        inteiroR = int(a.split()[0])
        somaR += inteiroR
    elif "S" in a:
        inteiroS = int(a.split()[0])
        somaS += inteiroS
totcob = somaC + somaS + somaR
mediaC = (somaC / totcob) * 100
mediaR = (somaR / totcob) * 100
mediaS = (somaS / totcob) * 100
print(f"Total: {totcob} cobaias")
print(f"Total de coelhos: {somaC}")
print(f"Total de ratos: {somaR}")
print(f"Total de sapos: {somaS}")
print(f"Percentual de coelhos: {mediaC:.2f} %")
print(f"Percentual de ratos: {mediaR:.2f} %")
print(f"Percentual de sapos: {mediaS:.2f} %")




