
while True:
    nome = str(input("Valor: ")).strip()
    palavra = ""
    contador = 0
    if nome == "" :
        print(f'ERRO: "{nome}" é um preço inválido')
        continue
    elif nome.isalpha():
        print(f'ERRO: "{nome}" é um preço inválido')
    else:
        for cont in nome:
            contador += 1
            if cont.isalpha():
                print(f'ERRO: "{nome}" é um preço inválido')
                break
            elif cont.isspace():
                print(f'ERRO: "{nome}" é um preço inválido')
                break
            elif cont == ",":
                palavra += "."
            elif cont == ".":
                palavra +=cont
            elif cont.isnumeric():
                palavra += cont
            if contador == len(nome):
                break
    if contador == len(nome):
        inteiro = float(palavra)
        break
print(f"O número é {inteiro:.2f}")









#def leiadinheiro(msg):
#    valido = False
#    while not valido:
#        entrada = str(input(msg))
#        if entrada.isalpha():
#            print(f'"{entrada}" é um preço inválido!')
#        else:
#            valido = True
#            return float(entrada)


