# Código para geração da sequência de Collatz

from time import sleep


def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1


def leiaint(n):
    while True:
        try:
            inteiro = int(input(n))
        except KeyboardInterrupt:
            print('\n\033[1:31mO usuário cancelou a operação.\033[m')
            return 3
        except (ValueError, TypeError):
            print('\033[1:31mERRO! Digite um número inteiro válido!\033[m')
        else:
            break
    return inteiro


number = leiaint('Digite um número inteiro: ')
while True:
    n = collatz(number)
    print(n)
    if n == 1:
        break
    else:
        number = n
    sleep(1)
