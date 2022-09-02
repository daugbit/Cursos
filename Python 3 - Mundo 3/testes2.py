def cabecalho():
    print('\033[1:39:42m~' * 30)
    print(f'{"SISTEMA DE AJUDA PyHELP":^30}')
    print('~' * 30)


def pyhelp(resp):
    from time import sleep
    tam = 40 + len(resp)
    print('\033[1:39:46m~' * tam)
    print(f'{"Acessando o manual do comando resp...":^50}')
    print('~' * (40 + len(resp)))
    sleep(0.5)
    print(f'\033[0:30:47m')
    print(help(resp))


while True:
    cabecalho()
    r = (str(input('\033[m> Função ou biblioteca: '))).strip().lower()
    if r == 'fim':
        print('\033[1:30:41m~' * 15)
        print(f'{"ATÉ LOGO!":^15}')
        print('~' * 15)
        break
    pyhelp(r)
