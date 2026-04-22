# 5. Crie uma função chamada contar_caracteres(texto) que receba uma string e retorne a quantidade de caracteres.

def contar_caracteres(texto):
    caracter = len(texto.replace(" ",""))
    return caracter

# Programa Principal
frase = str(input("Digite uma frase: "))
quantidade = contar_caracteres(frase)

print(f"A frase informada possue {quantidade} caracteres!")

