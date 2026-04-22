# -*- coding: utf-8 -*-

A , B = map(int,input().split())
Valordoproduto = 0
quantidade = B #"quantidade" recebe a quantidade que o usuário vai querer de determinado produto, Que será multiplicado pelo valor do produto

if A == 1:                                #Se "A" for igual a "1" significa que o produto é um Cachorro Quente e custa R$ 4.00
    Valordoproduto = 4.00 * quantidade
elif A == 2:                              #Se "A" for igual a "2" significa que o produto é um X-Salada e custa R$ 4.50
    Valordoproduto = 4.50 * quantidade
elif A == 3:                              #Se "A" for igual a "3" significa que o produto é um X-Bacon e custa R$ 5.00
    Valordoproduto = 5.00 * quantidade
elif A == 4:                              #Se "A" for igual a "4" significa que o produto é uma Torrada Simples e custa R$ 2.00
    Valordoproduto = 2.00 * quantidade
elif A == 5:                              #Se "A" for igual a "5" significa que o produto é um Refrigerante e custa R$ 1.50
    Valordoproduto = 1.50 * quantidade

print(f"Total: R$ {Valordoproduto:.2f}")

