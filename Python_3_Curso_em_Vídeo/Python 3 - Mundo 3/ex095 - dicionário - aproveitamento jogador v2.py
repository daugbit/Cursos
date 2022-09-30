player = {}
team = []
gols = []
while True:
    print('--' * 20)
    player['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Número de partidas que {player["nome"]} jogou: '))
    for i in range(0, partidas):
        gol = gols.append(int(input(f'Gols no jogo {i + 1}: ')))
    player['gols'] = gols.copy()
    player['total'] = sum(gols)
    gols.clear()
    team.append(player.copy())
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while r not in "SsNn":
        r = str(input('ERRO! Digite apenas S ou N: ')).strip().upper()[0]
    if r in "Nn":
        break
print('=-' * 30)
print(f'{"cód":^5} {"nome":^15} {"gols":^12} {"total":^15}')
print('-' * 50, end='')
for i, j in enumerate(team):
    print(f'\n{i + 1:^5}', end='')
    for k in j.values():
        print(f'{str(k):^15}', end='')
print()
print('-' * 50)
while True:
    r = int(input('De qual jogador você deseja visualizar os detalhes [999 para sair]? '))
    if r == 999:
        break
    elif r > len(team) or r < 1:
        print(f'Opção inválida! Digite um cód entre 1 e {len(team)}')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {team[r -1]["nome"]}:')
        for i, j in enumerate(team[r - 1]['gols']):
            print(f'No jogo {i + 1} fez {j} gols.')
        print('*' * 50)
