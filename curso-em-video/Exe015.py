km = int(input("Digite a quantidade de quilometros rodados: "))
dias=int(input("Digite a quantidade de dias que ficou com o carro: "))
carrodia = dias * 60
kmrodados = km * 0.15
total = carrodia + kmrodados
print (f"O valor total para pagar é de R${total:.2f} reais")
