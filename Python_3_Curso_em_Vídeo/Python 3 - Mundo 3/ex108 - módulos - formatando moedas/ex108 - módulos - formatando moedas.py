import moeda

price = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.currency(price)} é igual a {moeda.currency(moeda.metade(price))}')
print(f'O dobro de {moeda.currency(price)} é igual a {moeda.currency(moeda.dobro(price))}')
print(f'Aumentando 10%, o preço passa a ser {moeda.currency(moeda.aumento(price, 10))}')
print(f'Diminuindo 20%, o preço passa a ser {moeda.currency(moeda.reducao(price, 20))}')
