# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores
n = int(input("Digite um número: "))
contnumero = 1
maior = n
menor = n
media = n
r = str(input("Deseja continuar adicionando números? [S/N]")).upper()

while r == "S":
    n = int(input("Digite outro número: "))
    contnumero += 1
    media += n
    if maior < n:
        maior = n
    elif menor > n:
        menor = n
    r = str(input("Deseja continuar adicionando números? [S/N]")).upper()
media /= contnumero
print("")
print(f"A média dos números informados foi {media:.2f}")
print(f"O maior número foi {maior}")
print(f"O menor número foi {menor}")

