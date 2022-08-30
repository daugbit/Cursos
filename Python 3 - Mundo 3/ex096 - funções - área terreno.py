def area(x, y):
    a = x * y
    print('-' * 50)
    print(f'A área do terreno é de \033[4:32m{a:.2f}m²\033[m.')


def topo(msg):
    print('-' * 50)
    print(f'{msg:^50}')
    print('-' * 50)

topo('ANALISADOR DE TERRENO')
larg = float(input('Informe a largura do terreno (m): '))
comp = float(input('Informe o comprimento do terreno (m): '))
area(larg, comp)
