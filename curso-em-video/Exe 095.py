# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização
# de detalhes do aproveitamento de cada jogador
listaoriginal = []


while True:
    dicionario = {}
    somagols = 0
    lista = []
    nome = str(input("Nome do Jogador: "))
    partidas = int(input(f"Quantas partidas {nome} jogou? "))

    for cont in range(0,partidas):
        gol = int(input(f"Quantos gols na partida {cont}? "))
        lista.append(gol)
        somagols += gol
    dicionario['nome'] = nome
    dicionario['gols'] = lista
    dicionario['total'] = somagols
    listaoriginal.append(dicionario)

    resposta = str(input("Quer continuar? [S/N] ")).upper()
    if resposta == "N":
        break
    else:
        continue
print("-="*45)
print(f'{"cod nome":<15} {"gols":^23} {"total":>5}')
print("-"*45)


for posicao,valor in enumerate(listaoriginal):
    print(f"{posicao:<1} {valor['nome']:<12} {str(valor['gols']):^23} {valor['total']:>5}")
print("-"*45)

tamanho = len(listaoriginal)-1

while True:
    dados = int(input("Mostrar dados de qual jogador? "))
    if dados >= 0 and dados <= tamanho:
        print(f"-- LEVANTAMENTO DO JOGADOR {listaoriginal[dados]['nome']}")
        for pos,valor in enumerate(listaoriginal[dados]['gols']):
            print(f"  No jogo {pos} fez {valor} gols.")
    elif dados == 999:
        break
    else:
        print(f"ERRO! Não existe jogador com código {dados}! Tente novamente")
print("<<VOLTE SEMPRE>>")




