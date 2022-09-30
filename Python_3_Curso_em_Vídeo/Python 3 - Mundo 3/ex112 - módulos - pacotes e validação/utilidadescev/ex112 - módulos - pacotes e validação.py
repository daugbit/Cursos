import moeda
import dados

while True:
    price = str(input('Digite um preço: R$')).strip().replace(',', '.')
    verif_price = dados.dados(price)
    if not verif_price:
        print(f'\033[1;31mERRO!\'{price}\' não é um preço válido.\033[m')
    else:
        break
moeda.resumo(verif_price, 30, 45)
