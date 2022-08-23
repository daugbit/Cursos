tupla = (int(input('Digite um número: ')),
            int(input('Digite outro número: ')),
            int(input('Digite mais um número: ')),
            int(input('Digite um último número: ')))
pares = False
print('=-=' * 15)
print('A) O número 9 foi digitado', tupla.count(9), 'vez(es).')
if 3 in tupla:
    print(f'B) O primeiro número 3 foi digitado na posição {tupla.index(3) + 1}.')
else:
    print('B) Não foi digitado nenhum número 3.')
for num in tupla:
    if num % 2 == 0:
        pares = True
        break
if not pares:
    print('C) Não foram digitados números pares.')
else:
    print('C) Os valores pares digitados foram: ', end='')
    for num in tupla:
        if num % 2 == 0:
            print(num, end=' ')
