#Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão aritimética.
#No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input("Informe o primeiro número: "))
razao = int(input("Informe a razão: "))

print(primeiro)
soma = primeiro
for i in range(1,10):
    soma += razao
    print(soma)