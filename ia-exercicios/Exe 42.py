#Peça uma frase e mostre quantas palavras ela tem.
frase = str(input("Digite uma frase para saber quantas palavras ela tem: "))
lista = frase.split()
palavras = len(lista)

print(f"A frase tem {palavras} palavras")

