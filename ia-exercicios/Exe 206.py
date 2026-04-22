# 9. Crie uma função chamada saudacao_personalizada que receba dois parâmetros: nome e cargo.
# O parâmetro cargo deve ser opcional e, se não for passado, deve assumir o valor "Colaborador".
# A função deve retornar a mensagem: "Olá, [nome]! Cargo: [cargo]".

def saudacao_personalizada(nome,cargo="Colaborador"):
    return f"Olá, {nome}! Cargo {cargo}"

#Programa Principal
name = str(input("Informe seu nome: "))
profission = str(input("Informe seu cargo: "))
if profission.strip() == "":
    print(saudacao_personalizada(name))
else:
    print(saudacao_personalizada(name,profission))


#Concluido