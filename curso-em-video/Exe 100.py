#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
# e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda
# função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior
import random
from random import randint
from time import sleep
numeros = []

def sorteia():
    print("Sorteando 5 valores da lista:",end=" ")
    for cont in range(5):
        num = randint(1,10)
        numeros.append(num)
        print(num,end=" ")
        sleep(0.5)
    print("PRONTO!")

def somaPar():
    soma = 0
    print(f"Somando os valores de {numeros}, temos",end=" ")
    for cont in numeros:
        if cont % 2 == 0:
            soma += cont
    print(soma)

# Programa Principal
sorteia()
somaPar()