def metade(p):
    return p / 2


def dobro(p):
    return p * 2


def aumento(p, d):
    return p/100 * (100 + d)


def reducao(p, d):
    return p/100 * (100 - d)


def currency(p, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')
