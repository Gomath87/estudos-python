#Peça ao usuário 5 números e armazene em uma tupla.
#Mostre os números em ordem crescente
#Diga se o número 9 foi digitado e em qual posição (se tiver)
numeros = ()
for cont in range (5):
    n = int(input(f"Digite o {cont+1}º número: "))
    numeros = numeros + (n,)
print(f"A ordem crescente é {sorted(numeros)}")
if 9 in numeros:
    print(f"Ele aparece na posição {numeros.index(9)+1}")
else:
    print("O número 9 não foi digitado")
