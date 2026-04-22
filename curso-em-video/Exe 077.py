#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
#Para cada palavra, quais são as suas vogais.

palavras = ("aprender","programar", "linguagem", "python", "curso", "gratis", "estudar", "praticar", "trabalhar", "mercado", "programador","futuro")
vogais = 'aeiou'
for cont in palavras:
    print(f"Na palavra {cont.upper()} temos",end=" ")
    for letra in cont:
        if letra in vogais:
            print(f"{letra}",end=" ")
    print()
