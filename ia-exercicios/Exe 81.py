#Crie um programa que leia uma frase digitada pelo usuário e diga:
#Quantas vezes aparece a letra “a”
#Em que posição ela aparece pela primeira vez
#Em que posição ela aparece pela última vez

frase = str(input("Digite uma frase: ")).upper()
letrasA = frase.count("A")
posicaoA = frase.find("A")
posiçãoultimaA = frase.rfind("A")

print("A letra 'a' aparece")