# 2. Crie um dicionário com 5 palavras em inglês e suas traduções em português.
#    - Peça ao usuário para digitar uma palavra em inglês e mostre sua tradução.
#    - Caso a palavra não esteja no dicionário, informe "Não encontrado".

dicionario = {
    "Apple": "Maçã",
    "Dog": "Cachorro",
    "House": "Casa",
    "Book": "Livro",
    "Car": "Carro"}
resposta = str(input("Digite uma palavra em inglês: ")).title()
if resposta not in dicionario:
    print("Não encontrado")
else:
    print(f"A tradução da palavra {resposta} é {dicionario[resposta]}")