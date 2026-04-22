#Pegue o nome completo de uma pessoa e mostre:
#Nome com todas as letras maiúsculas
#Nome com todas as letras minúsculas
#Quantas letras tem (sem considerar espaços)

nome = str(input("Digite seu nome completo: "))
nometodomaiusculo = nome.upper()
nomeminusculo = nome.lower()
nomesemespacos = nome.replace(" ","")
quantidadedeletras = len(nomesemespacos)

print("Seu nome com todas as letras maiúsculas fica:",nometodomaiusculo)
print("Seu nome com todas as letras minúsculas fica:",nomeminusculo)
print("Seu nome possue",quantidadedeletras,"letras")


