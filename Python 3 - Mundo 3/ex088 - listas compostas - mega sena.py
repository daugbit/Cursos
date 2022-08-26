from random import randint
from time import sleep
print('=-' * 30)
print(f'{"MEGA SENA - geração de apostas randomizadas":^60}')
print('=-' * 30)
n_bets = int(input('Quantidade de jogos que você deseja: '))
bets = []
for bet in range(0, n_bets):
    bets.append([])
    for c in range(0, 6):
        while True:
            num = randint(1, 60)
            if num not in bets[bet][:c]:
                bets[bet].append(num)
                break
for c in range(0, n_bets):
    print(f'Números para o jogo {c + 1}: {sorted(bets[c])}')
    sleep(0.5)
