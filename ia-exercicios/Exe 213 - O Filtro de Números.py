#Crie um programa que peça ao usuário para digitar 5 números e os armazene
# em uma lista. Depois, o programa deve:
#Exibir a soma de todos os números.
#Exibir a média dos números.
#Criar uma nova lista contendo apenas os números que são maiores que 10.

lista = []
num = int
for cont in range (1,6):
    num = int(input(f"Digite o {cont}° número:"))
    lista.append(num)

maiordez = []
for cont in lista:
    if cont > 10:
        maiordez.append(cont)


print(f"A lista dos números digitados foram: {lista}")
print(f"A soma dos números é igual a {sum(lista)}")
print(f"A média dos números é igual a {sum(lista) / len(lista)}")
print(f"A lista contendo os números acima de 10 são: {maiordez}")
