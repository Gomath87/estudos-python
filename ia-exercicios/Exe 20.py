#Fatorial simples
#Peça um número e calcule o seu fatorial usando for.
#Ex.: 5! = 5×4×3×2×1 = 120

numero = int(input("Digite um número para saber seu respectivo fatorial: "))
fatorial = 1
for cont in range(numero,1,-1):
    fatorial *= cont
print(f"O fatorial do número {numero} é {fatorial}")


