r = ' '
total = thousand = cheapest_price = 0
print('====== LOJAS CARO PACARAI ======')
while True:
    product = str(input('Produto: ')).strip()
    price = int(input('Preço: R$'))
    if total == 0 or price < cheapest_price:
        cheapest = product
        cheapest_price = price
    total += price
    if price > 1000:
        thousand += 1
    while r not in 'sn':
        r = str(input('Deseja continuar? [s/n]')).strip().lower()[0]
    if r == 'n':
        break
    r = ' '
print('=-=' * 20)
print(f'''O total da compra foi de R${total}.
Temos {thousand} produto(s) que custa(m) mais de R$1 mil.
O produto mais barato foi {cheapest}, que custa R${cheapest_price}.''')