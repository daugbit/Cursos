from ex021_classes_agregacao_classes import CarrinhoCompras, Produto

carrinho = CarrinhoCompras()

p1 = Produto('Relógio', 199.5)
p2 = Produto('Camiseta', 120.99)
p3 = Produto('Calça', 80.6)
p4 = Produto('Boné', 50.9)
p5 = Produto('Sandália', 64.99)
p6 = Produto('Celular', 1849.5)
p7 = Produto('Notebook', 4999.9)

carrinho.add_produto(p1)
carrinho.add_produto(p2)
carrinho.add_produto(p3)
carrinho.add_produto(p4)
carrinho.add_produto(p5)
carrinho.add_produto(p4)
carrinho.add_produto(p3)
carrinho.add_produto(p2)
carrinho.add_produto(p1)
carrinho.add_produto(p7)
carrinho.add_produto(p6)


carrinho.lista_carrinho()
carrinho.subtotal()
