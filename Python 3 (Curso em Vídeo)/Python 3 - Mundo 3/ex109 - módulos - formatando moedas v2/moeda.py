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
