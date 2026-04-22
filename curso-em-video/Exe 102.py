# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro
# que indique o número a calcular e o outro chamada show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial

def fatorial(f,show=False):
    '''
    -> Calcula o Fatorial de um número.
    :param f: O número a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: O valor do Fatorial de um número n.
    '''
    multi = 1
    for cont in range(f,0,-1):
        multi *= cont
        if show == True:
            print(cont,end=" ")
            if cont > 1:
                print("x", end=" ")
            else:
                print("=", end=" ")
    return multi
#Programa Principal
print(fatorial(5,show=True))
