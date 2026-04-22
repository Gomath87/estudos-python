#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
if n1 > n2:
    maior = n1
    print(f"O número maior é o número {maior}")
elif n2 > n1:
    maior = n2
    print(f"O número maior é o número {maior}")
else:
    print("Não existe valor maior, pois os dois são iguais")