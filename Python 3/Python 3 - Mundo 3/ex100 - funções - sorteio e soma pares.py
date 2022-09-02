from random import randint
from time import sleep


def sorteio():
    for i in range(5):
        lista.append(randint(1, 9))
        print(lista[i], end=' ')
        sleep(0.5)
    print('PRONTO!')

def SomaPares(rel):
    pares = 0
    for i in rel:
        if i % 2 == 0:
            pares += i
    print(pares)


lista = []

print('Sorteando cinco números da lista:', end=' ')
sorteio()
print(f'Somando os valores pares de {lista}, temos ', end='')
SomaPares(lista)
