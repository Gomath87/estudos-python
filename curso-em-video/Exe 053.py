#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#EXE: APOS A SOPA
#     A SACADA DA CASA
#     O LOBO AMA O BOLO
#     ANOTARAM A DATA DA MARATONA

frase = str(input("Digite uma frase para saber se ela é um Palíndromo: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print("Temos um Palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")
