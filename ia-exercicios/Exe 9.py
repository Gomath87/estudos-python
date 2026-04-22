#Somar números
#Peça ao usuário para digitar 5 números. No final, mostre a soma total deles.
soma=0
for num in range (1,6):
    num = int(input(f"Digite o {num}o número: "))
    soma += num
print(f"A soma total dos números digitados foi {soma}")

