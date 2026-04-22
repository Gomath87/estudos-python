#Peça uma frase e mostre se ela começa com a palavra “Olá”
frase = str(input("Digite uma frase: ")).title() #Para garantir que a primeira letra de cada palavra seja em maiúscula!
raselista = frase.split()
if fraselista[0] =="Olá":
    print("A frase informada começa com a palavra 'Olá'")
else:
    print("A frase informada NÃO começa com a palavra 'Olá'")





###################################################################
#                         OUTRO MÉTODO PARA ENCONTRAR
###################################################################

frase = str(input("Digite uma frase: ")).title() #Para garantir que a primeira letra de cada palavra seja em maiúscula!
primeirapalavra = ""
for letra in frase:
    if letra != " ":
        primeirapalavra += letra
    else:
        break

if primeirapalavra == "Olá":
    print("A frase informada começa com a palavra 'Olá'")
else:
    print("A frase informada NÃO começa com a palavra 'Olá'")







###################################################################
#                         OUTRO MÉTODO PARA ENCONTRAR
###################################################################
frase = input("Digite uma frase: ").strip().title()
if frase.startswith("Olá"):
    print("A frase informada começa com a palavra 'Olá'")
else:
    print("A frase informada NÃO começa com a palavra 'Olá'")




