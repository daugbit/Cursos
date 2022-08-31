def leiaint(n):
    while True:
        for i in range(0, len(n)):
            if n[i] not in '0123456789':
                print('\033[1:31mERRO! Digite um número inteiro válido!\033[m')
                n = str(input('Digite um número: '))
                break
        if i == (len(n) - 1):
            break
    return n


num = leiaint(input('Digite um número: '))
print(f'Você acabou de digitar o número {num}.')
