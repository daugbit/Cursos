from random import randint
wins = 0
while True:
    pc = randint(0, 9)
    print('=-=' * 15)
    player = str(input('Par[P] ou ímpar[I]? ')).strip().upper()[0]
    player_n = int(input('Escolha um número: '))
    total = pc + player_n
    print(f'Computador: {pc} \n Total: {total}')
    if total % 2 == 0:
        result = 'PAR'
    else:
        result = 'ÍMPAR'
    if result == 'PAR' and player == 'P' or result == 'ÍMPAR' and player == "I":
        wins += 1
        print(f'{result:.^45} \n\033[1;32mVocê venceu!\033[m \nVamos mais uma...')
    else:
        print(f'{result:.^45} \n\033[1;31mGAME OVER\033[m \nVocê venceu {wins} vez(es).')
        break