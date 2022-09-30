lista = []
pares = []
impares = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    r = str(input('Quer continuar? [s/n] ')).strip().lower()[0]
    while r not in 'sn':
        r = str(input('Opção inválida! Deseja continuar? [s/n] '))
    if r == 'n':
        break
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        pares.append(lista[c])
    else:
        impares.append(lista[c])
print('=-=-' * 20)
print(f'A lista original digitada foi {lista}')
print(f'A lista de pares digitados foi {pares}')
print(f'A lista de ímpares digitados foi {impares}')
