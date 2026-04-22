# 2. Crie uma lista vazia.
#    - Pergunte 5 nomes de pessoas e idades.
#    - Armazene cada pessoa como uma lista dentro da lista principal.
#    - Mostre apenas as pessoas maiores de idade.

lista = []

for cont in range (1,6):
    listatemp = []
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    listatemp.append(nome)
    listatemp.append(idade)
    lista.append(listatemp)
print("As pessoas maiores de idade são: ")
print("")
for cont in lista:
    if cont[1] > 17:
        print(f"Nome:{cont[0]:<10} {cont[1]}")
