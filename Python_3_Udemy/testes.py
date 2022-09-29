def divisao(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError('o divisor não pode ser zero.')
    return n1 / n2


try:
    print(divisao(2, 0))
except ZeroDivisionError as error:
    print(f'Log: {error}')
