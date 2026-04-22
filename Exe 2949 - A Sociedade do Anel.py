# -*- coding: utf-8 -*-

n = int(input())
hobbit = humanos = elfos = anoes = magos = 0
for con in range (n):
    nome = str(input())
    a = nome[-1]
    if a == "X":
        hobbit += 1
    elif a == "H":
        humanos += 1
    elif a == "E":
        elfos += 1
    elif a == "M":
        magos += 1
    elif a == "A":
        anoes += 1
print(f"{hobbit} Hobbit(s)")
print(f"{humanos} Humano(s)")
print(f"{elfos} Elfo(s)")
print(f"{anoes} Anao(oes)")
print(f"{magos} Mago(s)")

