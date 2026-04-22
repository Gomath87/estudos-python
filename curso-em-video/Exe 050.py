#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
#que forem pares. Se o valor digitado for ímpar, desconsidere-o.
somapar = 0
for i in range(1,7,1):
    a = int(input(f"Digite o {i}.o número inteiro: "))
    if a % 2 == 0:
        somapar += a
print(f"Essa é a soma dos números pares: {somapar} ")


