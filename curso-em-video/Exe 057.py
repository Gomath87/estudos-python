# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
#Caso esteja errado, peça a digitação novamente ate ter um valor correto.

sexo = str(input("Informe seu sexo: ")).upper()
while sexo != "F" and sexo != "M":
    sexo = str(input("Caracteres inválidos por favor digite M ou F!")).upper()
print(f"Obrigado pela informação vc é do sexo {sexo}")




