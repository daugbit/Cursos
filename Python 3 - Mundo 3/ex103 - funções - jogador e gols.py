def player(name='<desconhecido>', goals='0'):
    print(f'O jogador {name} fez {goals} gol(s) no campeonato.')


jogador = str(input('Nome do jogador: '))
gols = str(input('Gols marcados: '))
if jogador != '' and gols != '':
    player(jogador, gols)
elif jogador != '' and gols == '':
    player(name=jogador)
elif jogador == '' and gols != '':
    player(goals=gols)
else:
    player()
