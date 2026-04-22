#3. Analisador de Nomes (Strings)
#Objetivo: Manipular strings como se fossem listas.
#Peça o nome completo de uma pessoa.
#O programa deve imprimir:
#O nome todo em maiúsculas.
#Quantas letras tem o nome (sem contar espaços).
#Apenas o primeiro nome.
#O nome invertido (Dica: use o fatiamento [::-1]).

nome = input("Digite seu nome completo: ").strip()

print(f"O nome maiúsculo é: {nome.upper()}")
nome2 = nome.replace(" ","")
print(f"A quantidade de letras sem contar os espaços é: {len(nome2)}")
print(f"O primeiro nome é: {nome.split()[0]}")
print(f"O nome invertido é {nome[::-1]}")

