from random import randint
from time import sleep
from operator import itemgetter
ranking = []
jogadas = {
            'jogador1': randint(1, 6),
            'jogador2': randint(1, 6),
            'jogador3': randint(1, 6),
            'jogador4': randint(1, 6)
            }
for k, i in jogadas.items():
    print(f'O {k} jogou {i}.')
    sleep(1)
print('-=' * 20)
print('Classificação final:')
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for k, i in enumerate(ranking):
    print(f'{k + 1}º lugar: {i[0]}, que tirou {i[1]}.')
