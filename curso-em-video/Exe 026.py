#Faça um programa que leia uma frase pelo teclado e mostre:    
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.
frase = input("Digite uma frase: ") .strip()  #     O gato brincou muito e dormiu em cima da mesa
print("A letra 'A' aparece",frase.lower().count("a"),"vezes")
print("A letra 'A' aparece pela primeira vez na posição: ",frase.lower().find("a"))
print("A letra 'A' aparece pela ultima vez na posição: ",frase.lower().rfind("a"))
