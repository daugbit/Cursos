from time import sleep

c = {'preto': '\033[m',
    'verde': '\033[1:39:42m',
    'azul': '\033[1:39:46m',
    'branco': '\033[0:30:47m',
    'vermelho': '\033[1:30:41m',
     }


def titulo(msg, cor='preto'):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c['preto'], end='')


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{r}\'...', 'azul')
    sleep(0.5)
    print(c['branco'], end='')
    print(help(com))


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 'verde')
    r = str(input('Função ou Biblioteca > ')).strip()
    if r.upper() == 'FIM':
        titulo('ATÉ LOGO', 'vermelho')
        break
    else:
        ajuda(r)
