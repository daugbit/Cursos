num = int(input('Digite um número: '))
count = 0
for c in range(1, num+1):
    if num % c == 0:
        count += 1
        print(f'\033[4;32m{c}\033[m', end=' ')
    else:
        print(f'\033[31m{c}\033[m', end=' ')
if count == 2:
    print(f'\nO número {num} É primo, pois só é divisível por 1 e por ele mesmo!')
elif count > 2:
    print(f'\nO número {num} NÃO é primo, pois é divisível por {count} divisores (verdes acima).')
