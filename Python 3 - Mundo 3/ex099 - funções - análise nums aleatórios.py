from random import randint


def maior():
    lista = []
    print('=-' * 30)
    print('Analisando os valores passados...')
    length = randint(0, 5)
    for i in range(length):
        lista.append(randint(0, 9))
        print(lista[i], end=' ')
    print(f'Foram informados {length} valores ao todo.')
    print(f'O maior valor informado foi {max(lista)}.')


run_times = randint(1, 10)
for i in range(0, run_times):
    maior()
