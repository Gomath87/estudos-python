#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Exe:
#Digite um número:1834
#unidade: 4
#Dezena: 3
#Centena: 8
#Milhar: 1
numero = str(input("Digite um número entre 0 e 9999: "))
tamanho = len(numero)

if tamanho == 1:
    print("Unidade ",numero[0])
elif tamanho == 2:
    print("Unidade ",numero[1])
    print("Dezena ", numero[0])
elif tamanho == 3:
    print("Unidade ",numero[2])
    print("Dezena ",numero [1])
    print("Centena ", numero[0])
elif tamanho == 4:
    print("Unidade ",numero[3])
    print("Dezena ",numero[2])
    print("Centena ",numero[1])
    print("Milhar ",numero[0])


