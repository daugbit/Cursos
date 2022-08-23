products = ('Pão', 4.99, 'Queijo', 10.9, 'Presunto', 10.5, 'Arroz', 15.80, 'Farinha', 18.5, 'Detergente', 2.35,
            'Bateria', 5.9, 'Sabão', 21.9, 'Mel', 8.8)
print('-' * 30)
print('LISTAGEM DE PREÇOS'.center(30))
print('-' * 30)
for product in range(0, len(products), 2):
    print(f'{products[product]:.<22}R$', end='')
    print(f'{products[product + 1]:>6.2f}')
print('-' * 30)
