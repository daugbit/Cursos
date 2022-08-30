from time import sleep


def cont(x, y, z):
    print('-=' * 30)
    print(f'Contagem de {x} até {y} de {z} em {z}:')
    for i in range(x, y + z, z):
        print(i, end=' ')
        sleep(0.5)
    print()


cont(1, 10, 1)

cont(10, 0, -2)

print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
start = int(input('Início: '))
end = int(input('Fim: '))
passe = int(input('Passo: '))
if passe == 0:
    passe = 1
if end < start:
    passe = passe * (-1)
if end > start and passe < 0:
    passe = passe * (-1)

cont(start, end, passe)

print(f'{"FIM DA CONTAGEM":*^50}')
