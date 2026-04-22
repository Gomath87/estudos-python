# 6. Crie um dicionário com nomes de times e a quantidade de pontos que possuem.
#    Mostre qual time tem mais pontos.

tabela = {"Santos":50,"Corinthians":35,"São Paulo":80,"Flamento":70,"Botafogo":55}

for time,ponto in tabela.items():
    if time == "Santos":
        lider = time
        maior = ponto
    else:
        if ponto > maior:
            lider = time
            maior = ponto

print(f"O time que tem mais pontos é o {lider} com {maior} pontos")