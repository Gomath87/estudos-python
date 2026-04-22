# 9. Peça ao usuário para digitar uma frase.
#    - Mostre a posição da primeira ocorrência da letra "o".

frase = input("Digite uma frase: ").lower()
if "o" in frase:
    print(f"A primeira incidência da letra 'o' na frase está na posição {frase.index('o')+1}")
else:
    print("A frase informada não possui a letra 'o'")
