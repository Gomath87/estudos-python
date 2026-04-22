# Crie uma tupla com 10 letras (sem repetir).
#Peça ao usuário para digitar uma letra e diga se ela está ou não na tupla.

letras = ("a","b","c","d","e","f","g","h","i","k")
letra = str(input("Digite uma letra para saber se ela está na tupla: ")).strip().lower()
if letra in letras:
    print(f"A letra '{letra}' está na tupla")
else:
    print(f"A letra '{letra}' não está na tupla")

