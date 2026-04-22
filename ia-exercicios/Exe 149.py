# 9. Crie um dicionário com 5 estados brasileiros e suas capitais.
#    Peça ao usuário um estado e mostre a capital correspondente.

estados = {"Pernambuco":"Recife","São Paulo":"São Paulo","Maranhão":"São Luis","Amazonas":"Manaus","Rio Grande do Norte":"Natal"}

print(estados.keys())
resposta = str(input("Qual capital de qual estado desejas ver? ")).title()
print(f"A capital de {resposta} é {estados[resposta]}")
