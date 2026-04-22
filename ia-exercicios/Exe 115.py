# 11. Peça ao usuário para digitar uma frase.
#     - Verifique se a palavra "python" está presente na frase.

frase = input("Digite uma frase: ").lower()
palavras = frase.split()
if 'python' in palavras:
    print("Contém a palavra 'python'")
else:
    print("Não contém a palavra 'python'")