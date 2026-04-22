# Peça uma frase e substitua todas as letras “a” por “@”.
from dataclasses import replace

frase = str(input("Digite uma frase: "))
frasedois = frase.replace("a","@").replace("A","@")
print("")
print(f"Frase original: {frase}")
print(f"Frase modificada: {frasedois}")

