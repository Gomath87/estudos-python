#Peça uma frase e diga quantas vezes aparece
# a letra “a” (tanto maiúscula quanto minúscula).
from itertools import count

frase = str(input("Digite uma frase: ")).upper()
print(f"A frase informada aparecem {frase.count("A")} vezes a letra 'a'")

