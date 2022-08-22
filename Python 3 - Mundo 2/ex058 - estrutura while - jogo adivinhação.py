from random import randint
from time import sleep
num = randint(1, 10)
bets = 1
print('PENSANDO EM UM NÚMERO ENTRE 1 E 10......')
sleep(2)
bet = int(input('Adivinhe o número em que eu pensei: '))
while bet != num:
    bets += 1
    if bet < num:
        print('Mais...', end=' ')
    elif bet > num:
        print('Menos...', end=' ')
    bet = int(input('Tente mais uma vez: '))
print(f'ACERTOU! \nVocê precisou de \033[4m{bets}\033[m tentativas até acertar.')
if bets <= 3:
    print('Você é muito bom nesse jogo!')
elif bets <= 6:
    print('Nada mal, hein.')
elif bets <=9:
    print('Mais sorte na próxima vez.')
elif bets == 10:
    print('Você é horrível nesse jogo!')
