# 3. Crie uma lista com 15 números aleatórios entre 1 e 50.
#    - Mostre os números únicos (sem repetições) e quantas vezes cada número apareceu.
from itertools import count
from random import randint
lista = []
listaunicos = []
for cont in range (0,15):
    num = randint(1,50)
    lista.append(num)
    if num not in listaunicos:
        listaunicos.append(num)
print(f"Números únicos: {listaunicos}")

for cont in listaunicos:
    quantidade = lista.count(cont)
    print(f"O número {cont} aparece {quantidade} vezes")


