#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
from operator import index

num = (int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")),
       int(input("Digite um número: ")), int(input("Digite um número: ")),)

print(f"Você digitou os valores {lista}")
print(f"O valor 9 apareceu {num.count(9)} vezes")

if 3 in num:
    posicao = num.index(3)+1
    print(f"O valor 3 foi digitado na {posicao}ª posição")
else:
    print("O valor 3 não foi digitado em nenhuma posição")
print("Os números pares digitados foram ", end="")
for cont in num:
    if cont % 2 == 0:
        print(cont, end=" ")



