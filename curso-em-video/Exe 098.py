# Faça um programa que tenha uma função chamada contador()
# que recebe três parâmetros:início,fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada.
import time


def contador(ini, fim, pas):
    print("-=" * 17)
    print(f"Contagem de {ini} até {fim} de {abs(pas)} em {abs(pas)}")

    if ini > fim:
        for cont in range(ini, fim - 1, -pas):
            print(cont, end=" ")
            time.sleep(0.5)
        time.sleep(0.5)
        print("FIM!")

    elif ini < fim:
        for cont in range(ini, fim + 1, pas):
            print(cont, end=" ")
            time.sleep(0.5)
        time.sleep(0.5)
        print("FIM!")


# programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print("Agora é sua vez de personalizar a contagem!")

inicio = int(input("Início: "))
conclusao = int(input("Fim: "))
passo = int(input("Passo: "))
if passo == 0:
    passo = 1
else:
    passo = abs(passo)
contador(inicio, conclusao, passo)


