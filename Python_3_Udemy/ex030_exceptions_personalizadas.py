class MeuError(Exception):
    ...


class OutroError(Exception):
    ...


def raise_():
    exception_ = MeuError('Minha exception personalizada')
    raise exception_


raise_()

try:
    raise_()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)
    print()
    exception_ = OutroError('Vou lançar de novo')
    #raise exception_ from error