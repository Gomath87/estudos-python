#Contar quantos números são pares e quantos são ímpares
#Peça ao usuário digitar, por exemplo, 10 números e no final diga:

#Quantos eram pares

#Quantos eram ímpares
par = 0
impar = 0
print("Digite 10 números: ")
for cont in range(1,11):
    n=int(input(f"{cont}º número: "))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print(f"A quantidade de números Pares digitados são {par}, e Ímpares {impar}")




