lista = []
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        print('Número adicionado com sucesso!')
        r = str(input('Deseja continuar? [s/n] ')).strip().lower()[0]
        while r not in 'sn':
            r = str(input('Opção inválida! Deseja continuar? [s/n] '))
        if r == 'n':
            break
    elif num in lista:
        print(f'O número {num} já está na lista. Não vou adicioná-lo.')
print('=-=-' * 20)
print(f'Você digitou os valores {sorted(lista)}')
