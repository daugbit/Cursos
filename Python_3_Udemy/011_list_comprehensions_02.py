"""
Programa que rececbe uma lista de compras, com nome e preços dos produtos
individuais, e retorna o valor total da compra utilizando list comprehension.
"""
cart = []
while True:
    product = []
    product.append(input('Produto: '))
    product.append(int(input('Preço: R$')))
    product = tuple(product)
    cart.append(product)
    r = input('Deseja continuar as compras? (s/n) ').strip()[0]
    if r in 'SsNn':
        if r in 'Ss':
            continue
        else:
            break
    else:
        while r not in 'SsNn':
            r = input('Opção inválida. Digite apenas s ou n: ').strip()[0]
        if r in 'Nn':
            break

total = sum([valor[1] for valor in cart])
print(total)
