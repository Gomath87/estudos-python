#10. Repetir uma mensagem
#Peça uma mensagem e um número. Mostre essa mensagem repetida aquele número de vezes.
#Ex.: Digita "Olá" e 5 → O programa escreve "Olá" 5 vezes.
mensagem = str(input("Digite uma frase: "))
numero = int(input("Digite um número: "))

for con in range(1,numero+1):
    print(mensagem)


