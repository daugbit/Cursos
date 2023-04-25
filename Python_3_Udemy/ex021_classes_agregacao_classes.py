class CarrinhoCompras:
    def __init__(self):
        self.carrinho = []

    def add_produto(self, produto):
        self.carrinho.append(produto)

    def lista_carrinho(self):
        print('=' * 30)
        print('CARRINHO DE COMPRAS'.center(30))
        print('=' * 30)
        for produto in self.carrinho:
            print(produto.name.ljust(18), 'R$', str(produto.preco).rjust(8))
        print('=' * 30)

    def subtotal(self):
        total = 0
        for produto in self.carrinho:
            total += produto.preco
        print('SUBTOTAL'.ljust(18), 'R$', str(total).rjust(8))


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
