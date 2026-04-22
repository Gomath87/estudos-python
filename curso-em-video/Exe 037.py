#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#-1 para binário
#-2 para octal
#-3 para hexadecimal
numero = int(input("Digite um número: "))
opcao = int(input("Se você deseja transformar esse número em binário digite '1'. Para octal é o '2'. Para hexadecimal é o '3'"))

if opcao == 1:
    bina = bin(numero)
    print(f"O número {numero} para binário é igual a {bina}")
elif opcao == 2:
    octa = oct(numero)
    print(f"O número {numero} para octal é igual a {octa}")
elif opcao == 3:
    hexa = hex(numero)
    print(f"O número {numero} para hexadecimal é igual a {hexa}")
else:
    print("Por favor digite um número entre 1 a 3")
