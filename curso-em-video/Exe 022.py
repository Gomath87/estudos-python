#Crie um programa que leia o nome completo de uma pessoa e mostre:    OK
#O nome com todas as letras maiusculas                                OK
#O nome com todas minísculas                                          OK
#Quantas letras ao todo (sem considerar espaços)                      OK
#Quantas letras tem o primeiro nome                                   OK

nome = str(input("Digite seu nome completo: ")).strip()
print("Seu nome em maiusculo é: ",nome.upper())
print("Seu nome em maiusculo é: ",nome.lower())
print("Seu nome tem ao todo ",len(nome) - nome.count(" ")," letras")

primeiro = (nome.split()[0])
print("O primeiro nome tem: ",len(primeiro)," letras")



