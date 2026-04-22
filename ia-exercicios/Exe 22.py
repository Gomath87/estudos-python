#Soma de vários números
#Peça ao usuário quantos números ele quer somar, depois peça os números e mostre a soma total.
quant = int(input("Informe quantos números deseja somar: "))
soma = 0
for cont in range(1,quant+1):
    n = float(input(f"Digite o {cont}º número: "))
    soma += n
print(f"A soma dos números informados é {soma:.1f}")

