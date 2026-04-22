#🎯 Peça uma frase e uma letra, e diga quantas vezes a letra aparece.

frase = str(input("Digite uma frase: ")).upper()
letra = str(input("Digite uma letra: ")).upper()

quantidade = frase.count(letra)
print(f"Na frase informada a letra {letra} se repete {quantidade} vezes")