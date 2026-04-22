# 6. Crie uma função chamada calcular_media(lista) que receba uma lista de números e retorne a média deles.

def calcular_media(lista):
    soma = 0
    for cont in lista:
        soma += cont
    divisao = soma / len(lista)
    return divisao


# Programa Principal
numeros=[]

for cont in range(1,6):
    num = int(input(f"Digite o {cont} número: "))
    numeros.append(num)

resultado = calcular_media(numeros)

print(f"A média dos números informados é {resultado:.1f}")


