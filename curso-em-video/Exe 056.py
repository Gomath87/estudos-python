#Desenvolva um programa que leia, nome, idade, e sexo de 4 pessoas. No final do
#programa, mostre:
#A média de idade do grupo.
#Qual é o nome do homen mais velho.
#Quantas mulheres têm menos de 20 anos.

Midade = 0
media = 0
Velho = 0
Maior = 0
r = 0
for dados in range(1,5):
    nome = str(input(f"Qual o nome da {dados}o pessoa:"))
    idade = int(input(f"informe a idade de {nome}: "))
    sexo = str(input(f"""Com que gênero você se indentifica {nome}?  \nDigite:    M para Masculino e F para Feminino: """)).upper()

    # A média de idade do grupo.
    Midade += idade               #Aqui vai somando as idades de guardando nessa variável (Midade)
    if dados == 4:                #Aqui coma a condição, se o laço ''dados'' estiver na posição 4, então vai realizar a média logo abaixo
        media = Midade / 4        #Media vai receber a soma das idades (Midade) dividido por 4.

    # Qual é o nome do homen mais velho.
    if sexo == "M":                #Algorítmo para achar a pessoa do sexo masculino mais Velha, caso tenha uma pessoa do sexo Masculino
        if dados == 1:             #
            Maior = idade          #
            Velho = nome           #
        else:                      #
            if idade > Maior:      #
                Maior = idade      #
                Velho = nome       #
                result = 1         #Se houver um homem result recebera 1 ai vc cra um if para mostrar a resposta na conclusão, e para chamar o resultado no final, digite Velho para mostrar o nome e Maior para dizer quantos anos ele tem
    else:                          #
        result = 0                 #Caso não for digitado nenhum dados de uma pessoa do sexo masculino result vai receber "0", e o if criado abaixo para mostrar a resposta

    # Quantas mulheres têm menos de 20 anos.
    if sexo == "F":
        if idade < 20:
            r += 1

#Resultado
print("")
print("")
print(f"A média de idades do grupo é de {media} anos")

if result == 1:
    print(f"O nome do homem mais velho é {Velho} com {Maior} anos!")
else:
    print("Não foi armazenado nenhum dados de pessoa do sexo Masculino")

if r >= 1:
    print(f"Existem {r} mulheres abaixo de 20 anos")
else:
    print(f"Não existe nenhuma mulher abaixo de 20 anos")

















