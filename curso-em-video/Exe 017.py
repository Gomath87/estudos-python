import math
op = int(input("Digite o valor do cateto oposto: "))
a = int(input("Digite o valor do cateto adjacente: "))
hipo = math.sqrt(math.pow(op,2) + math.pow(a,2))
print (f"O comprimento da hipotenusa é: {hipo:.2f}")

