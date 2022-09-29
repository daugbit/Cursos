def funcao1(funcao):
    return funcao()


def funcao2(*args):
    return 'Oi'


var = funcao1(funcao2)
print(var)
