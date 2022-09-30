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


file = '005_history.txt'

cabecalho()
with open(file, 'a') as file_object:
    while True:
        status = ''
        status += (strftime('%d %b %Y %H:%M:%S', localtime()))
        try:
            urllib.request.urlopen(site)
        except urllib.error.URLError:
            status += (f' - O site {name} não está acessível no momento.\n')
        else:
            status += (f' - O site {name} está acessível no momento.\n')
        finally:
            print(status, end='')
            file_object.write(status)
            sleep(time)