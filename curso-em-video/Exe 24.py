#crie um programa que leia um nome de uma cidade e dia se ela começa ou não com o nome"SANTO".
cidade = input("Digite um nome de cidade: ").strip() #.strip() remove espaços extras
print(cidade.lower().startswith("santo")) #.lower() deixa tudo minúsculo      #.startswith("santo") verifica se começa com essa palavra


cidade = input("Digite um nome de cidade: ")
s = cidade.split()[0]
print("Santo" in s)
