#Carrinho de Compras Simples
#Objetivo: Praticar o loop while e o método .append().
#Crie uma lista vazia chamada carrinho.
#Crie um loop que peça para o usuário digitar um produto para adicionar ao carrinho.
#Se ele digitar "sair", o loop para e exibe a lista de compras ordenada alfabeticamente.

carrinho = []
produto = ""
while produto != "sair":
    produto = input("Digite um produto: ")
    if produto == "sair":
        break
    carrinho.append(produto)
carrinho.sort()
print(f"A lista de produtos é: {carrinho}")