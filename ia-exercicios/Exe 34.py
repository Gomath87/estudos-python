 #2. Caixa registradora simples
 #Crie um programa que:
 #Peça o preço de vários produtos
 #O programa deve continuar pedindo até que o usuário digite 0
 #No final, mostre:
 #A soma total
 #Quantos produtos foram cadastrados
 #Qual foi o produto mais caro

preco = float(input("Digite o valor do produto: "))
quantidade = 1
soma = preco
caro = preco
r = int(input("Deseja informar o valor de outro produto?[1=SIM e 0 =NÃO]"))

while r != 0:
    preco = float(input("Digite o valor do produto: "))
    soma += preco
    quantidade += 1
    if caro < preco:
        caro = preco
    r = int(input("Deseja informar o valor de outro produto?[1=SIM e 0 =NÃO]"))
print(f"A soma total dos valores dos produtos foi {soma:.2f}")
print(f"Foram cadastrados {quantidade} produtos")
print(f"O produto mais caro foi {caro:.2f}")



