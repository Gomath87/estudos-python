# 5. Crie uma função chamada "formata_preco" que receba um valor numérico e um símbolo de moeda opcional (default="R$").
# A função deve retornar o valor formatado com duas casas decimais e vírgula como separador decimal.
# Exemplo: formata_preco(1234.5) → "R$1.234,50"

def formata_preco(preco,moeda="R$"):
    preco = f"{preco:.2f}"
    preco = str(preco)
    preco = preco.replace(".",",")
    s = moeda+preco
    return s

#programa principal
num = float(input("Informe um preço: "))
moed = input("Informe uma moeda: ")
if moed == "":
    resultado = formata_preco(num)
else:
    resultado = formata_preco(num,moed)
print(f"O preço formatado é {resultado}")
