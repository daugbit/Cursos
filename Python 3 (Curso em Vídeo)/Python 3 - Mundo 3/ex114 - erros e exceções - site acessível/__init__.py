#! /usr/bin/python3

import urllib.request
import urllib.error
from time import sleep, localtime, strftime


def cabecalho():
    global name, site, time
    print('-' * 50)
    print('SISTEMA DE MONITORAMENTO DE WEBSITES'.center(50))
    print('-' * 50)
    name = str(input('Identificador: '))
    site = str(input('Endereço: '))
    time = int(input('Intervalo (s): '))
    print('-' * 50)


cabecalho()
while True:
    print(strftime('%d %b %Y %H:%M:%S', localtime()), end=' - ')
    try:
        urllib.request.urlopen(site)
    except urllib.error.URLError:
        print(f'\033[31mO site {name} não está acessível no momento.\033[m')
    else:
        print(f'\033[32mO site {name} está acessível no momento.\033[m')
    finally:
        sleep(time)
