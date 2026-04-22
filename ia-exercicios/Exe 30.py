#3. Maior e menor número
#Peça ao usuário 5 números e mostre:
#Qual é o maior
#Qual é o menor
maior = 0
menor = 0
for cont in range(1,6):
    num = int(input(f"Digite o {cont}o número:"))
    if cont == 1:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
print(f"O maior número é {maior} e o menor {menor}")


