jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input(f'Número de partidas que {jogador["nome"]} jogou: '))
for i in range(0, jogador['partidas']):
    gol = gols.append(int(input(f'Gols no jogo {i + 1}: ')))
jogador['gols'] = gols.copy()
jogador['aproveitamento'] = sum(gols)
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for i in range(0, jogador['partidas']):
    print(f'  => No jogo {i + 1}, fez {jogador["gols"][i]} gols')
print(f'Foi um total de {jogador["aproveitamento"]} gols.')
