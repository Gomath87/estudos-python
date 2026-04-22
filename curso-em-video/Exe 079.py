#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exist lá dentro, ele
#não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
while True:
    valor = int(input("Digite um valor: "))
    if valor in lista:
        print("Valor duplicado! Não vou adicionar...")
    else:
        lista.append(valor)
        print("Adicionado com sucesso...")
    resposta = str(input("Quer continuar? [S/N] ")).lower()
    if resposta == "s":
        continue
    else:
        break
print("-="*40)
print(f"Você digitou os valores {sorted(lista)}")


