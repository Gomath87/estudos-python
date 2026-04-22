# Crie um programa que vai ler vários números e colocar em uma lista
# Depois disso, mostre:
# A) Quantos números foram digitados
# B) A lista de valores, ordenada de forma decrescente
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
r = str
while r != "N":
    num = int(input("Digite um valor: "))
    lista.append(num)
    r = str(input("Deseja continuar? [S/N] ")).upper()
reverso = sorted(lista, reverse=True)
print("-="*45)
print(f"Você digitou {len(lista)} elementos")
print(f"Os valores em ordem decrescente é {reverso}")
if 5 in lista:
    print("O valor 5 faz parte da Lista!")
else:
    print("O valor 5 não faz parte da Lista")
