
sq = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
current_player = 'X'
plays = 9

def screen_view():
    for i in range(3):
        print(f'|{sq[i][0]}|{sq[i][1]}|{sq[i][2]}|')


def play(n):
    global current_player, plays
    if sq[n] == sq[n]:
        sq[n] = current_player
        # current_player = 'O' if current_player == 'X' else current_player = 'X'
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
        plays =- 1
    else:
        print('Jogada inválida')


def verific():
    pass


while True:
    screen_view()
    play(str(input(f'Onde o Jogador {current_player} vai jogar? ')))
    winner = verific()
