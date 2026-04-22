# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(*a):
    print("-="*30)
    tamanho = len(a)
    if tamanho == 0:
        print("Analisando os valores passados...")
        print(f"Foram informados {"0"} valores ao todo.")
        print(f"O maior valor informado foi {"0"}")
    else:
        maximo = max(a)
        for cont in a:
            print(cont,end=" ")
            sleep(0.3)
        print("")
        print("Analisando os valores passados...")
        print(f"Foram informados {tamanho} valores ao todo.")
        print(f"O maior valor informado foi {maximo}")

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
