# 2. Crie um dicionário com 5 palavras e suas traduções em inglês.
#    Peça ao usuário uma palavra em português e mostre sua tradução.

palavras = {"cat":"gato" , "dog":"cachorro", "table":"mesa", "apple":"maçã", "lemon":"limão"}
print("-="*40)
print("Palavras disponíveis:", list(palavras.keys()))
resposta = str(input("Qual palavra deseja ver o significado? ")).lower()
if resposta in palavras:
    print(f"A tradução da palavra {resposta} é {palavras[resposta]}")
else:
    print("Essa palavra não está no dicionário.")
print("-="*40)