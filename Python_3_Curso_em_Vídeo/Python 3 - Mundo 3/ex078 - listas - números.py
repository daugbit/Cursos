lista = []
for c in range(0, 4):
    num = int(input(f'Digite um número para a posição {c}: '))
    lista.append(num)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)}, nas posiçãoes:', end=' ')
for c in range(0, 4):
    if lista[c] == max(lista):
        print(f'{c}...', end=' ')
print(f'\nO menor valor digitado foi {min(lista)}, nas posições:', end=' ')
for c in range(0, 4):
    if lista[c] == min(lista):
        print(f'{c}...', end=' ')
