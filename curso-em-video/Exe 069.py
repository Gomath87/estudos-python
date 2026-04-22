# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
maior = 0
homem = 0
mulhermenosvinte = 0
print("---" * 8)                                   #Estético
print("   CADASTRE UMA PESSOA   ")
print("---" * 8)                                   #Estético
#-----------------------------------------------------------
while True:
    idade = int(input("Idade: "))                  #Pergunta e armazena o valor da Idade
#-----------------------------------------------------------
    sexo = str(input("Sexo: [M/F]")).upper()       #Pergunta e armazena O valor da resposta
    while True:                                    #Esse laço de repetição garante que o programa só prossiga se o usuário digitar M ou F. Caso seja diferente ele vai continuar repetindo a pergunta
        if sexo != "M" and sexo != "F":
            sexo = str(input("Sexo: [M/F]")).upper()
        else:
            break                                  #Se for digitado M ou F o comando ''Break'' vai parar o Laço de repetição!
    print("---" * 8)                               #Estético
#-----------------------------------------------------------
    resp = str(input("Quer continuar? [S/N] ")).upper()            #Pergunta e armazena a resposta
    while True:                                                    #Esse laço de repetição garante que o programa só prossiga se o usuário digitar S ou N. Caso seja diferente ele vai continuar repetindo a pergunta
        if resp != "S" and resp != "N":
            resp = str(input("Quer continuar? [S/N] ")).upper()
        else:
            break                                                  #Se for digitado "S" ou "N" o comando "Break" vai parar o laço de repetição

    # -----------------------------------------------------------
    if idade > 18:
        maior += 1                       #Aqui trabalha os dados
    if sexo == "M":                    # A) Quantas pessoas tem mais de 18 anos.
        homem += 1                       # B) Quantos homens foram cadastrados.
    if sexo == "F" and idade < 20:     # C) Quantas mulheres tem menos de 20 anos.
        mulhermenosvinte += 1

    # -----------------------------------------------------------



#-----------------------------------------------------------
    if resp == "N":
        break                           #Aqui se a reposta a pergunta "DESEJA CONTINUAR?" for negativa esse "break" para o principal laço de repetição que começa na linha 14 e finaliza aqui!
    print("---" * 8)
#-----------------------------------------------------------
print("==="*2,"FIM DO PROGRAMA","==="*2)
print(f"Total de pessoas com mais de 18 anos: {maior}")

if homem > 1:                                             #Essa estrutura de condição trata a se a resposta vai ser no plural ou no singular, caso "homem" tenha valor maior que 1, significa que existe mais de um homem, logo a resposta será no plural, caso tenha o valor de 1 significa que a resposta será no sigular, e caso possua o valor de 0, será apresentado a resposta "Não foi cadastrado nenhum homem!"
    print(f"Ao todo temos {homem} homens cadastrados")
elif homem == 1:
    print(f"Ao todo temos {homem} homem cadastrado")
else:
    print("Não foi cadastrado nenhum homem!")

if mulhermenosvinte > 1:                                  #Essa estrutura de condição trata a se a resposta vai ser no plural ou no singular, caso "mulhermenosdevinte" tenha valor maior que 1, significa que existe mais de uma mulher, logo a resposta será no plural, caso tenha o valor de 1 significa que a resposta será no sigular, e caso possua o valor de 0, será apresentado a resposta "Não possue nenhuma mulher abaixo de 20 anos!"
    print(f"E temos {mulhermenosvinte} mulheres com menos de 20 anos")
elif mulhermenosvinte == 1:
    print(f"E temos {mulhermenosvinte} mulher com menos de 20 anos")
else:
    print("Não possue nenhuma mulher abaixo de 20 anos!")




