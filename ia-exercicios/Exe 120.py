print("-"*28)
print(" "*8,"CARDÁPIO"," "*8)
print("-"*28)

print("Panquecada         R$ 25,00")
print("Omelete            R$  5,00")
print("Misto Quente       R$  2,50")
print("Vitamina           R$  3,00")
print("Suco               R$  2,00")
print("-"*28)
print("")
panquecada = omelete = mistoquente = vitamina = suco =  0
while True:
    print("Por favor digite apenas um ítem por vez")
    item = str(input("Informe um item [caso deseje parar digite '0']")).upper().strip()
    if item == "0":
        break
    else:
        quantidade = int(input("Informe a quantidade: "))
        if item == 'PANQUECADA':
            panquecada += quantidade
        elif item == 'OMELETE':
            omelete += quantidade
        elif item == 'MISTO QUENTE':
            mistoquente += quantidade
        elif item == 'VITAMINA':
            vitamina += quantidade
        elif item == 'SUCO':
            suco += quantidade

preco1 = panquecada * 25.00
preco2 = omelete * 5.00
preco3 = mistoquente * 2.50
preco4 = vitamina * 3.00
preco5 = suco * 2.00
total = preco1 + preco2 + preco3 + preco4 + preco5

pedido = (panquecada, omelete, mistoquente, vitamina, suco)
nomes = ("Panquecada", "Omelete", "Misto Quente", "Vitamina", "Suco")

print("-"*25)
print("SEU PEDIDO: ")
print("")
for i,qtd in enumerate(pedido):
    if qtd > 0:
        print(f"{qtd} {nomes[i]}")
print("")
print(f"Total: {total:.2f}")
print("-"*25)











