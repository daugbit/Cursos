vel = int(input('Velocidade do automoóvel (km/h): '))
if vel >= 80:
    ticket = (vel-80)*7
    print(f'O condutor recebeu uma multa de R${ticket}')
else:
    print('Velocidade dentro dos limites da via')
