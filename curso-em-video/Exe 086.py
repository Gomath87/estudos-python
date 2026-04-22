# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
lista = [[],[],[]]
pos = 0

while True:
    for cont in range (0,3):
        num = int(input(f"Digite um valor para [{pos},{cont}]: "))
        lista[pos].append(num)
    pos += 1
    if pos == 3:
        break

print("-="*40)
pos = 0

while True:
    for cont in lista[pos]:
        print(f"[  {cont:^5}  ]",end=" ")
    print("")
    if pos == 2:
        break
    pos += 1

