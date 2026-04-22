# Faça um programa que leia NOME e PESO de várias pessoas, guardando tudo em uma lista.No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas   #Igual ou acima de 100kg
# C) Uma listagem com as pessoas mais leves     #Igual ou abaixo de 70kg
lista = []
temp = []
pesado = []
leve = []
while True:
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))
    temp.append(nome)
    temp.append(peso)
    lista.append(temp[:])
    temp.clear()
    resposta = str(input("Quer continuar? [S/N]")).upper()
    if resposta == "N":
        break
print(f"Ao todo, você cadastrou {len(lista)} pessoas")

maximo = lista[0] [1]
minimo = lista[0] [1]

for cont in lista:
    if cont[1] >= 100:
        pesado.append(cont[0])
        if cont[1] > maximo:
            maximo = cont[1]
    elif cont[1] <= 70:
        leve.append(cont[0])
        if cont[1] < minimo:
            minimo = cont[1]

print(f"O maior peso foi de {maximo}Kg. Peso de {pesado}")
print(f"O menor peso foi de {minimo}Kg. Peso de {leve}")










