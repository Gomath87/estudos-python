# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre
# uma mensagem com tamanho adaptável.
#
# EX:
# escreval("Olá,Mundo!")
#Saida:
#------------
# Olá,Mundo!
#------------

def escreva(txt):
    tamanho = (len(txt)+4)
    print("~"*tamanho)
    print(f"  {txt}  ")
    print("~"*tamanho)

escreva("Olá Mundo!")
escreva("Bem vindo a linguagem de Python")
escreva("Olá")
