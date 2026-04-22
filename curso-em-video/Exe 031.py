#Desenvolva um programa que pergunte a ditância de uma viagem em KM.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200KM
#e R$ 0,45 para viajens mais longas (Acima de 200km)

distancia = float(input("Informe a distância da sua viagem: "))

if distancia <= 200:
    preco = distancia * 0.50
    print(f"O preço da sua passagem será de R${preco:.2f}")
else:
    preco = distancia * 0.45
    print(f"O preço da sua viajem será de R${preco:.2f}")
print("Seja bem vindo a aviação Trans Javali Cansado!")