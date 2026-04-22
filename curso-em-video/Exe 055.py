#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual
#foi o MAIOR e o MENOR peso lidos.
maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}ª pessoa: "))

    if i == 1:
        # Na primeira pessoa, o maior e menor são iguais ao primeiro peso lido
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O maior peso lido foi {maior} Kg")
print(f"O menor peso lido foi {menor} Kg")
