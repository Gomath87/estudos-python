# 1. Crie uma função chamada saudacao() que receba um parâmetro opcional 'nome'.
# Se o nome for fornecido, mostre "Olá, nome!", caso contrário, mostre "Olá, visitante!".

def saudacao (nome="visitante"):
    if not nome.strip():  # verifica se é vazio ou só espaços
        nome = "visitante"
    print(f"Olá, {nome}!")

n = str(input("Digite seu nome: "))
saudacao(n)
