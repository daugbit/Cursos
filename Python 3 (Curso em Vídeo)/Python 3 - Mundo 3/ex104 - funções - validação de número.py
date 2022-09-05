def leiaint(n):
    while not n.isnumeric():
        print('\033[1:31mERRO! Digite um número inteiro válido!\033[m')
        n = str(input('Digite um número: '))
    return n


num = leiaint(input('Digite um número: '))
print(f'Você acabou de digitar o número {num}.')
