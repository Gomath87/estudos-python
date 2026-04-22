#Contagem personalizada
#Peça três números: início, fim e passo.
#Faça uma contagem com esses dados.
#Exemplo: início = 2, fim = 10, passo = 2 → 2, 4, 6, 8, 10.

inicio = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))
passo = int(input("Digite o valor do passo: "))

for cont in range(inicio,fim+1,passo):
    print(cont,end=" ")
