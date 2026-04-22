# Reescreva a função leiaint() que fizemos no desafio 104, incluindo
# agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")
        except KeyboardInterrupt:
            print("\033[0;31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            a = float(input(msg))
            return a
        except KeyboardInterrupt:
            print("\033[0;31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        except:
            print("\033[0;31mERRO! Digite um número real válido.\033[m")


#Programa principal
n = leiaint("Digite um Inteiro: ")
a = leiafloat("Digite um Real: ")
print(f"O valor inteiro digitado foi {n} e o real foi {a}")

