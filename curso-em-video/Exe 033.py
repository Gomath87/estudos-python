#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceiro número inteiro: "))

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:  #Acha o maior número
    maior = n2
else:
    maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:   #Acha o menor número
    menor = n2
else:
    menor = n3
print(f"O maior número é {maior} e o menor número {menor}")