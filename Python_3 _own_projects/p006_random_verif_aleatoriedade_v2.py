from random import randint

table = {
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


def randomize(times):
    global table
    for i in range(times):
        n = str(randint(1, 9))
        table[n] += 1


amostragem = int(input('Amostragem: '))
randomize(amostragem)

table_list = [[n, o] for n, o in table.items()]

table_list.sort(key=lambda x: x[1], reverse=True)

for item in table_list:
    print(f'{item[0]}: {item[1]}')
