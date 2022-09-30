first = int(input('Digite o primeiro termo: '))
ratio = int(input('Digite a Razão: '))
for c in range(first, first + ratio * 10, ratio):
    print(c)
