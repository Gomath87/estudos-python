#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
#Exe: Ana Maria de Souza
#Ultimo: Souza
nome = input("Digite seu nome completo: ").strip()
frase = nome.split()
print(frase[0],frase[-1])
