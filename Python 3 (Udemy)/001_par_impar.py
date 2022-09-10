while True:
    try:
        num = int(input('Digite um número inteiro: '))
    except ValueError:
        print('Você deve digitar apenas um número inteiro.')
    else:
        if num % 2 == 0:
            print(f'O número {num} é par.')
        else:
            print(f'O número {num} é ímpar.')
        break
print('FIM DO PROGRAMA')
