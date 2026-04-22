# 12. Peça ao usuário para digitar seu nome completo.
#     - Mostre quantas letras tem o nome (sem contar espaços).
nome = input("Digite seu nome completo: ")
nome = nome.replace(" ","")
print(f"Seu nome possue {len(nome)} letras")