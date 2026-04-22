#Peça ao usuário para digitar 5 produtos para uma lista de compras.
#Depois, mostre a lista completa e pergunte qual produto ele deseja remover.
#Remova o produto escolhido e mostre a lista atualizada.

compras = []

for produto in range(1,6):
    produtos = str(input(f"Digite o {produto}° produto: ")).title()
    compras.append(produtos)

while True:
    print(f"Segue a lista das compras {compras}")
    resposta = str(input("Deseja remover algum produto da lista? [S/N]: ")).upper()
    if resposta == "S":
        removerproduto = str(input("Qual o nome do produto que deseja remover? ")).title().strip()
        if removerproduto in compras:
            compras.remove(removerproduto)
        else:
            print("Produto não encontrado na lista.")
    else:
        break

