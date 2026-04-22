#Quantas letras?
#Peça uma palavra e mostre:
#Quantas letras tem
#Mostre cada letra uma por linha
palavra = str(input("Digite uma palavra: ")).strip(" ")
letras = len(palavra)
for letras in palavra:
    print(letras)