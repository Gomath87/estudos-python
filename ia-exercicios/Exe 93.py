# 9. Crie uma tupla com as vogais (a, e, i, o, u).
#    - Peça ao usuário uma palavra e mostre quais vogais aparecem e quantas vezes cada uma.

vogais = ("a","e","i","o","u")
palavra = str(input("Digite uma palavra: "))

for v in vogais:
    if v in palavra:
        print(f"A vogal '{v}' aparece {palavra.count(v)} vez(es).")
