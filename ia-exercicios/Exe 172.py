# 1. Crie uma função chamada soma(a, b) que receba dois números como parâmetros.
#    - A função deve retornar a soma dos dois números.
#    - Peça dois números ao usuário e mostre o resultado da função.

def soma(a,b):
    s = a+b
    print(s)


num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma(num1,num2)
