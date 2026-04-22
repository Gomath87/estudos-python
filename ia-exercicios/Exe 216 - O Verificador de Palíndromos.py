#Peça ao usuário para digitar uma palavra ou frase e verifique se ela é um
# palíndromo (se lê da mesma forma de trás para frente, como "arara" ou "radar").

#Dica: Em Python, você pode inverter uma string usando o fatiamento string[::-1]

palavra = input("Digite uma palavra para verificar se a mesma é um palíndromo: ").lower()
palavrainvertida = palavra[::-1]

if palavrainvertida == palavra:
    print("A palavra digitada É um palíndromo")
else:
    print("A palarva digitada NÃO é um palíndromo")