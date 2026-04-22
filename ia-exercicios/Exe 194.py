# 3. Crie uma função chamada fatorial() que receba dois parâmetros:
# o número a ser calculado e um valor lógico opcional show.
# Se show=True, mostre o cálculo do fatorial passo a passo; se False, apenas retorne o valor.

def fatorial(a, show=True):
    multiplicacao = 1
    for cont in range(a, 0, -1):
        multiplicacao *= cont
        if show:
            if cont != 1:
                print(f"{cont} X ", end="")
            else:
                print(f"{cont} = {multiplicacao}")
    return multiplicacao

# Programa principal
num = int(input("Digite um número para saber seu respectivo fatorial: "))
r = input("Deseja ver o cálculo? [S/N] ").upper()
show = True if r == "S" else False

resposta = fatorial(num, show)

# Imprime o resultado caso show=False
if not show:
    print(f"O fatorial de {num} é {resposta}")


