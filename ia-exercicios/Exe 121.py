from random import randint

numeroaleatorio = randint(1,100)
resp = int(input("Adivinhe o número que pensei ele está entre 1 e 100"))
if resp == numeroaleatorio:
    print(f"Caramba você acertou de primeira!, o número pensado foi realmente {numeroaleatorio}")
else:
    print("Que pena você não acertou")

for cont in range (2,8):
    resp = int(input("Tente novamente!: "))
    if resp == numeroaleatorio:
        print(f"Caramba você acertou de primeira!, o número pensado foi realmente {numeroaleatorio}")




