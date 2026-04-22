#1. Contar pares e ímpares
#Peça 10 números ao usuário e mostre:
#Quantos eram pares
#Quantos eram ímpares
par = 0
impar = 0
for cont in range(1,11):
    numero = int(input("Digite 10 números: "))
    if cont % 2 == 0:
        par += 1
    else:
        impar += 1
print(f"Ao todo foram {par} números pares e {impar} números ímpares!")

