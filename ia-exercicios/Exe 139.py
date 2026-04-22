
# 8. Crie uma lista com os itens de um cardápio ["Pizza","Suco","Hambúrguer","Sorvete"].
#    Pergunte ao usuário o que ele deseja pedir.
#    Verifique se está na lista e responda de acordo.

cardapio = ["Pizza","Suco","Hambúrguer","Sorvete"]

resposta = str(input("O que você deseja pedir? ")).lower().title()
if resposta in cardapio:
    print("Temos no cardápio")
else:
    print("Não temos no cardápio.")