import moeda

price = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.currency(price)} é igual a {moeda.metade(price, True)}')
print(f'O dobro de {moeda.currency(price)} é igual a {moeda.dobro(price, False)}')
print(f'Aumentando 10%, o preço passa a ser {moeda.aumento(price, 10, True)}')
print(f'Diminuindo 20%, o preço passa a ser {moeda.reducao(price, 20, False)}')
