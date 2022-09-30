import moeda

price = float(input('Digite um preço: R$'))
print(f'A metade de R${price} é igual a R${moeda.metade(price)}')
print(f'O dobro de R${price} é igual a R${moeda.dobro(price)}')
print(f'Aumentando 10%, o preço passa a ser R${moeda.aumento(price, 10)}')
print(f'Diminuindo 20%, o preço passa a ser R${moeda.reducao(price, 20)}')
