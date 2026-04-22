#🎯 4. Adivinhar Número
#Peça um número de 1 a 10:
#Se o número for igual ao que você definiu como correto (ex.: 7), exiba "Acertou!"
#Se for menor, diga "Tente um número maior"
#Se for maior, diga "Tente um número menor"

numero = 7
n = int(input("Digite um número entre 1 a 10: "))

if n < numero:
    print("Tente um número maior!")
elif n > numero:
    print("Tente um número menor!")
else:
    print("Parabéns Você acertou!")

