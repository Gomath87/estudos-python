#3. Validação de dados
#Peça para o usuário digitar seu sexo (M ou F).
#Se digitar algo diferente, continue pedindo até digitar um valor válido.

sexo = str(input("Digite seu sexo [M/F]: ")).upper()
while sexo != "M" and sexo != "F":
    sexo = str(input("Por favor digite um caractere válido [M/F]")).upper()
print("programa finalizado")


