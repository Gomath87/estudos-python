#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
posicoesmaximo = []
posicoesminimo = []
for cont in range(0,5):
    lista.append(int(input(f"Digite um valor para a posição {cont}: ")))
print("=-"*30)
maximo = max(lista)
minimo = min(lista)
print(f"Você digitou os valores {lista}")
for indice,valor in enumerate(lista):
    if maximo == valor:
        posicoesmaximo.append(indice)
    if minimo == valor:
        posicoesminimo.append(indice)
print(f"O maior valor digitado foi {maximo} nas posições {posicoesmaximo}...")
print(f"O menor valor digitado foi {minimo} nas posições {posicoesminimo}...")


