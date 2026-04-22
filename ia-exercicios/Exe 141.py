# 10. Peça ao usuário para digitar o nome de produtos até que ele digite "fim".
#     Guarde todos em uma lista.
#     Mostre todos os produtos digitados e quantos foram no total.
lista = []
while True:
    produto = str(input("Digite um produto: "))
    lista.append(produto)
    r = str(input("Dejesa continuar adicionando? [S/N] ")).upper()
    if r == "N":
        break
print(lista)
print(len(lista))
