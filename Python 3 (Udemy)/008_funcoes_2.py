def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def saudacao(nome):
    return f'Bom dia, {nome}!'


def recepcao(nome, saudacao):
    return f'{saudacao}, {nome}'


run = mestre(saudacao, 'Douglas')
print(run)

run2 = recepcao('Douglas', 'Seja bem-vindo')
print(run2)
