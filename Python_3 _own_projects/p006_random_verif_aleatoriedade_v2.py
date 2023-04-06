from random import randint

table = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
}
table_list = []

def randomize(times):
    global table
    for i in range(times):
        n = str(randint(0, 9))
        table[n] += 1


def organize():
    global table_list
    table_list = [[n, o] for n, o in table.items()]
    table_list.sort(key=lambda x: x[1], reverse=True)
    for i in table_list:
        i.append(round(i[1] / amostragem * 100, 2))


def summary():
    print('=-' * 15)
    print('QUADRO DE OCORRÊNCIAS'.center(30))
    print('=-' * 15)
    print('nº'.center(5), 'Ocorrências'.center(15), 'Taxa'.center(10))
    print('-' * 30)
    for i in table_list:
        print(f'{i[0]}'.center(5),
              f'{i[1]}'.center(15),
              f'{i[2]:.2f}%'.rjust(8),
              )


amostragem = int(input('Amostragem: '))
randomize(amostragem)
organize()
summary()
print(f'\n{table_list.__sizeof__()} bytes.')

