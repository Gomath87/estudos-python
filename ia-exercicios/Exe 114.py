frase = input("Digite uma frase: ").lower()
if "o" in frase:
    print(f"A última ocorrência da letra 'o' está na posição {frase.rindex('o') + 1}")
else:
    print("A letra 'o' não está presente na frase.")