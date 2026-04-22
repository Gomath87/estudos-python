#Peça para o usuário digitar uma frase qualquer. O seu programa deve contar quantas vogais (a, e, i, o, u)
# existem nessa frase e mostrar o total.
#Dica: Você pode usar um loop for para percorrer cada letra da string e verificar se ela
# está em uma lista de vogais.

frase = input("Digite uma frase: ").lower()
somavogais = 0
for cont in frase:
    if cont in "aeiou":
        somavogais += 1

print(f"Na frase digitada possui {somavogais} vogais")

