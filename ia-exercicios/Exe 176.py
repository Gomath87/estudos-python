# 5. Crie uma função chamada maior_numero(lista) que receba uma lista de números.
#    - A função deve retornar o maior número da lista.
#    - No programa principal, peça ao usuário para digitar 10 números e mostre o maior.

def maior_numero(lista):
    return max(lista)



a = [2,5,4,6,8,7,5,1,0]
resultado = maior_numero(a)
print(f"O maior número da lista é: {resultado}")


