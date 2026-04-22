# Peça ao usuário para digitar 5 nomes e guarde-os em uma lista.
# Depois, peça um nome para buscar e diga se ele está ou não na lista.
lista = []
for cont in range (1,6):
    nomes = str(input(f"Digite o {cont}° nome: ")).title().strip()
    lista.append(nomes)

resposta = str(input("Digite um nome para buscar na lista: ")).title().strip()

if resposta in lista:
    print(lista)
    print(f"O nome {resposta} está na lista.")
else:
    print(lista)
    print(f"O nome {resposta} não está na lista.")
