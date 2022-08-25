matriz = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        num = int(input(f'Digite um número para a posição [{i}, {j}]: '))
        matriz[i].append(num)
print('-=' * 20)
for i in matriz:
    print(f'[{c[0]:^5}] [{c[1]:^5}] [{c[2]:^5}]')
