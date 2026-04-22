#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
#da casa, o salário do comprador e em quatos anos ele vai pagar.
#Calcule o valor da prestação mensal. Sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.
#
print("-=-" * 10)                                            #Agradabilidade Visual
print ("Empréstimo Bancário")                                #Agradabilidade Visual
print("-=-" * 10)                                            #Agradabilidade Visual
casa = float(input("Qual o valor da casa? "))                #Informações
salario = float(input("Qual o valo do seu salário? "))       #Informações
ano = int(input("Quantos anos você vai pagar a casa? "))     #Informações
casadivanosmes = (casa / ano) / 12
trintapcentsal = (30/100) * salario
emprestimo = trintapcentsal - casadivanosmes

if emprestimo > 0:
    print("Parabéns, seu empréstimo foi aceito pelo Banco Javali Cansado!")
    print(f"O valor da prestação mensal é de {casadivanosmes}")
elif emprestimo == 0:
    print("Seu empréstimo foi aceito!")
    print(f"O valor da prestação mensal é de {casadivanosmes}")
else:
    print("Infelizmente seu empréstimo não foi aceito!")




