import random, sys
aliens = []
new_alien = {}
color = ['green', 'yellow', 'grey']
speed = ['slow', 'medium', 'fast']
for alien_number in range(1, 31):
    new_alien = {'id': ('alien' + str(alien_number)),
                 'color': random.choice(color),
                 'speed': random.choice(speed),
                 'points': random.randint(1, 9),
                 }
    aliens.append(new_alien)
for i in aliens:
    print('-*' * 20)
    for j, k in i.items():
        print(f'{j}: {k}')
