# 5. Crie uma função maior_numero que receba três números e retorne o maior entre eles.
# Use parâmetros opcionais para que, se nenhum número for passado, o valor padrão seja 0 para todos.

def maior_numero(a=0,b=0,c=0):
    lista = [a,b,c]
    maior = max(lista)

    return maior

#Programa Principal
n1 = str(input("Digite o primeiro número: "))
n1 = int(n1) if n1.strip() != "" else 0
n2 = str(input("Digite o segundo número: "))
n2 = int(n2) if n2.strip() != "" else 0
n3 = str(input("Digite o terceiro número: "))
n3 = int(n3) if n3.strip() != "" else 0

resposta = maior_numero(n1,n2,n3)
print(f"O maior número digitado foi {resposta}")





#Concluido