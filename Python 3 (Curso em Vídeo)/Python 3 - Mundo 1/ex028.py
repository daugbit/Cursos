from random import randint
from time import sleep
num = randint(1, 5)
print('Pensando.....')
bet = int(input('Entre 0 e 5, adivinhe o número no qual eu pensei: '))
print('PROCESSANDO...')
sleep(1)
if bet == num:
    print('Acertou, miserávi!')
else:
    print(f'ERROOOOOU!!!!! Era {num}')
