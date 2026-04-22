#Elabore um progrma que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#-À vista dinheiro/cheque: 10% de desconto
#-À vista no cartão: 5% de desconto
#-Em até 2x no cartão: preço normal
#-3x ou mais no cartão: 20% de juros

valor = float(input("Qual o valor do produto? "))
print("-=-" * 17)
print("       PAGAMENTO       ")
print("-=-" * 17)
print("Digite 1 para: Dinheiro/Cheque (10% de desconto)")
print("Digite 2 para: A vista no cartão (5% de desconto)")
print("Digite 3 para: 2x no cartão (Preço normal)")
print("Digite 4 para: 3x ou mais no cartão: 20% de juros")
opcao = int(input("Digite o número respectivo a sua forma de pagamento: "))

if opcao == 1:
    porcento = valor * (10 / 100)
    total = (valor - porcento)
    print(f"O valor de R${valor:.2f} com desconto de 10% fica: R${total:.2f}")
elif opcao == 2:
    porcento = valor * (5 / 100)
    total = (valor - porcento)
    print(f"O valor de R${valor:.2f} com desconto de 5% fica: R${total:.2f}")
elif opcao == 3:
    print(f"O valor da sua compra é: R${valor:.2f}")
elif opcao == 4:
    num = int(input("Quantas parcelas deseja dividir? "))
    if num >= 3:
        porcento = valor * (20 / 100)
        total = (valor + porcento)
        parcelas = (total / num)
        print(f"O valor de R${valor:.2f} com o acréscimo de 20% de juros fica: R${total:.2f}, compra parcelada em {num}X de R${parcelas:.2f}")
    else:
        print("Para essa opção, o número de parcelas deve ser 3 ou mais.")
else:
    print("Por favor digite um número entre 1 a 4")
print(" ")
print("Após a confirmação de pagamento seu comprovante será impresso")

