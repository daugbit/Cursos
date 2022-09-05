lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    r = str(input('Quer continuar? [s/n] ')).strip().lower()[0]
    while r not in 'sn':
        r = str(input('Opção inválida! Deseja continuar? [s/n] '))
    if r == 'n':
        break
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}.')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 NÃO faz parte da lista.')

