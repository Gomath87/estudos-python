# Faça um programa que leia NOME e MÉDIA de um aluno, guardando
# também a situação em um dicionário. No final, mostre o conteúdo
# da estrutura na tela.

dicionario = dict()

nome = str(input("Nome: "))
media = float(input(f"Média de {nome}: "))

dicionario["nome"] = nome
dicionario["media"] = media

print(f"Nome é igual a {dicionario['nome']}")
print(f"Média é igual a {dicionario['media']}")
if dicionario["media"] >= 7:
    print("Situação é igual a Aprovado")
elif dicionario['media'] < 7 and dicionario['media'] > 5:
    print("Situação é igual a Recuperação")
else:
    print("Situação é igual a Reprovado")
