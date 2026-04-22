#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print ("-----PAR ou ÍMPAR????-----")
print(" ")
n = int(input("Digite um número e descubra se ele é par ou ímpar:"))
print("-" * 30) #Apenas para deixar visualmente agradável
if n % 2 == 0:
    print(f"O número {n} é PAR!")
else:
    print(f"O número {n} é ÍMPAR!")
print("Programa Finalizado!")