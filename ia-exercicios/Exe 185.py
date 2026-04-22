# 9. Crie uma função chamada eh_palindromo(palavra) que verifique se uma palavra é palíndromo (igual de trás para frente).

def eh_palindromo(palavra):
    reverso = palavra[::-1]
    if reverso.upper() == palavra.upper():
        print(f"A palavra {palavra} é palindromo")
    else:
        print(f"A palavra {palavra} não é palindromo")

# Programa Principal
a = str(input("Digite uma palavra: "))
eh_palindromo(a)
