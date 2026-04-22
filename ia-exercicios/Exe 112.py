# 8. Peça ao usuário para digitar uma frase.
#    - Mostre quantas vezes aparece a letra "e".

frase = input("Digite uma frase: ").lower()
print(f"A frase informada possui exatamente {frase.count('e')} letras 'e'")