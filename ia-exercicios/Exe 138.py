# 7. Crie uma lista com 20 números aleatórios de 1 a 10.
#    Mostre quantas vezes o número 5 aparece.
from random import randint

lista = []
cinco = 0
for cont in range(1,21):
    num = randint(1,10)
    lista.append(num)
for cont in lista:
    if cont == 5:
        cinco+=1
print(f"O número 5 aparece {cinco} vezes")