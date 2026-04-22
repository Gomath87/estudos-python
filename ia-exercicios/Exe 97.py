# 14. Peça ao usuário 5 números e armazene-os em uma tupla.
#     - Mostre os números em ordem crescente.
#     - Mostre os números em ordem decrescente.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
n5 = int(input("Digite o quinto número: "))
numeros = (n1,n2,n3,n4,n5)
print(sorted(numeros))
print(sorted(numeros,reverse=True))
