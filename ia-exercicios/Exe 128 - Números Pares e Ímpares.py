#Peça ao usuário para digitar 10 números e armazene-os em uma lista.
#Depois, crie duas listas novas: uma com os números pares e outra com os números ímpares.
#Mostre as duas listas.
numeros = []
par = []
impar = []

for cont in range (1,11):
    numero = int(input(f"Digite o {cont}° número: "))
    numeros.append(numero)
    if cont % 2 == 0:
        par.append(cont)
    else:
        impar.append(cont)
print(f"Lista com todos os número {numeros}")
print(f"Lista com os números pares {par}")
print(f"Lista com os números ímpares {impar}")

