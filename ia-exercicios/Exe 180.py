# 4. Crie uma função chamada maior_numero(a, b, c) que receba três números e retorne o maior deles.

def maior_numero(a,b,c):
    lista = [a,b,c]
    maior = max(lista)
    return maior

# Programa Principal
a = []
for cont in range(1,4):
    num = int(input(f"Digite o {cont}° número: "))
    a.append(num)

resultado = maior_numero(a[0],a[1],a[2])
print(f"O maior número digitado foi: {resultado}")
