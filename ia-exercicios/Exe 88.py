# 3. Peça ao usuário para digitar 4 números inteiros e armazene-os em uma tupla.
#    - Mostre quantas vezes apareceu o número 9.
#    - Mostre a posição do primeiro número 3, caso exista.
#    - Mostre todos os números pares digitados.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))
n4 = int(input("Digite outro número: "))

tupla = (n1,n2,n3,n4)

print(f"O número 9 apareceu {tupla.count(9)} vezes")
if 3 in tupla:
    print(f"O número 3 está na posição {tupla.index(3)+1}")
else:
    print("O número 3 não está na tupla")
print("Os números pares digitados foram: ",end="")
for num in tupla:
    if num % 2 == 0:
        print(num,end=" ")
