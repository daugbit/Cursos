"""
Programa que verifica a taxa de ocorrência de números entre 0 e 9 gerados aleatoriamente
pelo módulo random, a partir de uma amostragem informada pelo usuário.
"""
from random import randint
lista = []
tabela = []


def randomize(times):
    """
    Gera uma lista com os números gerados aleatoriamente.
    param times: amostragem desejada pelo usuário.
    """
    global lista
    for i in range(times):
        lista.append(randint(0, 9))


def tab(times):
    """
    Tabula as ocorrências de cada número entre 0 e 9 gerados pela função randomize().
    param times: amostragem desejada pelo usuário.
    """
    global tabela
    for i in range(0, 10):
        sublist = []
        sublist.append(i)
        sublist.append(lista.count(i))
        sublist.append((sublist[1] / times) * 100)
        tabela.append(sublist)
    tabela.sort(key=lambda i: i[2], reverse=True)


def summary(lista):
    """
    Organiza, em formato de tabela, as informações geradas pelas funções
    randomize() e tab().
    """
    print('=-' * 15)
    print('QUADRO DE OCORRÊNCIAS'.center(30))
    print('=-' * 15)
    print('nº'.center(5), 'Ocorrências'.center(15), 'Taxa'.center(10))
    print('-' * 30)
    for i in lista:
        print(f'{i[0]}'.center(5),
              f'{i[1]}'.center(15),
              f'{i[2]:.2f}%'.rjust(8),
              )


n = int(input('Amostragem: '))
randomize(n)
tab(n)
summary(tabela)
print(f'\n{lista.__sizeof__()} bytes.')
