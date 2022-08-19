from random import choice
from emoji import emojize
from time import sleep
jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
pc = choice(jokenpo)
if pc == 'PEDRA':
    pc_emoji = emojize(':fist:', language='alias')
elif pc == 'PAPEL':
    pc_emoji = emojize(':hand:', language='alias')
else:
    pc_emoji = emojize(':v:', language='alias')
print('=-=' * 10)
print('''1 - PEDRA
2 - PAPEL
3 - TESOURA''')
print('=-=' * 10)
player = input('O que você vai querer jogar? ')
if player == "1":
    player = 'PEDRA'
    player_emoji = emojize(':fist:', language='alias')
elif player == "2":
    player = 'PAPEL'
    player_emoji = emojize(':hand:', language='alias')
else:
    player = 'TESOURA'
    player_emoji = emojize(':v:', language='alias')
print('        JO-', end='')
sleep(0.5)
print('KEN-', end='')
sleep(0.5)
print('PÔ')
sleep(0.5)
print(f'(pc) {pc} {pc_emoji}  X  {player_emoji} {player} (você)')
if pc == player:
    print('        \033[1;30;47mEMPATE!\033[m')
elif pc == "PEDRA" and player == "PAPEL" or pc == "PAPEL" and player == "TESOURA" or pc == "TESOURA" and player == "PEDRA":
    print('             \033[1;30;42mVocê venceu!\033[m')
else:
    print('\033[1;30;41mEu venci!\033[m')
