#Crie um programa que mostra na tela todos os números pares que estão no intervalo
#entre 1 e 50.

for a in range(1,51):
    if a % 2 == 0:        # FIZ USANDO UM IF QUE CALCULA PARA SABER
        print(a)
print("Esses são os números pares que estão no intervalo entre 1 e 50")




for a in range(2, 51, 2):
    print(a)               #MAS O GEPETO FEZ ASSIM COM O PASSO "2" ELE GARANTE QUE PERCORRA SÓ OS NÚMEROS PARES
print("Esses são os números pares que estão no intervalo entre 1 e 50")