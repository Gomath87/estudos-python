# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores Pares e os valores Ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
listaoriginal = []

while True:
    num= int(input("Digite um número: "))
    listaoriginal.append(num)
    r = str(input("Quer continuar? [S/N] ")).upper()
    if r == "N":
        break
    else:
        continue

listapares = []
listaimpares = []

for cont in listaoriginal:
    if cont % 2 == 0:
        listapares.append(cont)
    else:
        listaimpares.append(cont)

print("-=" *45)
print(f"A lista completa é {listaoriginal}")
print(f"A lista de pares é {listapares}")
print(f"A lista de ímpares é {listaimpares}")


