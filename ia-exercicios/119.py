print()
print("-" * 15,"CAIXA ELETRÔNICO","-"*15)
print()
cedulas = int(input("Qual valor você deseja sacar? "))
cedulas50 = cedulas20 = cedulas10 = cedulas1 = 0
cedulas2 = cedulas
print(f"Para sacar R${cedulas2:.2f} ")

while cedulas > 0:

    if cedulas >= 50:
        cedulas50 = cedulas // 50
        cedulas = cedulas % 50
        print(f"{cedulas50}x notas de R$50,00")

    elif cedulas >= 20:
        cedulas20 = cedulas // 20
        cedulas = cedulas % 20
        print(f"{cedulas20}x notas de R$20,00")

    elif cedulas >= 10:
        cedulas10 = cedulas // 10
        cedulas = cedulas % 10
        print(f"{cedulas10}x notas de R$10,00")

    elif cedulas >= 1:
        cedulas1 = cedulas // 1
        cedulas = cedulas % 1
        print(f"{cedulas1}x notas de R$1,00")







