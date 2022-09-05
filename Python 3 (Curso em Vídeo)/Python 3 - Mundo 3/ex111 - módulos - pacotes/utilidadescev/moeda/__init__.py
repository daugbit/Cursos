def resumo(price, a=0, d=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print('Preço analisado:'.ljust(16), currency(price).rjust(13))
    print('Dobro do preço:'.ljust(16), dobro(price).rjust(13))
    print('Metade do preço:'.ljust(16), metade(price).rjust(13))
    print(f'{a}% de aumento:'.ljust(16), aumento(price, a).rjust(13))
    print(f'{d}% de desconto:'.ljust(16), reducao(price, d).rjust(13))
    print('-' * 30)


def metade(p, format=True):
    resp = p / 2
    if format:
        resp = currency(resp)
    return resp


def dobro(p, format=True):
    resp = p * 2
    if format:
        resp = currency(resp)
    return resp


def aumento(p, d=0, format=True):
    resp = p/100 * (100 + d)
    if format:
        resp = currency(resp)
    return resp


def reducao(p, d=0, format=True):
    resp = p/100 * (100 - d)
    if format:
        resp = currency(resp)
    return resp


def currency(amount, moeda='R$'):
    return f'{moeda}{amount:.2f}'.replace('.', ',')
