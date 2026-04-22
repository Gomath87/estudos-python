#7. Peça uma frase e mostre a primeira palavra.
frase = str(input("Digite uma frase: "))
lista = frase.split()
print(f"A primeira palavra da frase digitada é {lista[0]}")
