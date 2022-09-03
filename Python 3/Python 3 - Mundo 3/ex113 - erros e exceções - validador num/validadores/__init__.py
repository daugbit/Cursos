def leiaint():
    while True:
        try:
            inteiro = int(input('Digite um número inteiro: '))
        except KeyboardInterrupt:
            print('\n\033[1:31mO usuário cancelou a operação.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[1:31mERRO! Digite um número inteiro válido!\033[m')
        else:
            break
    return inteiro


def leiafloat():
    while True:
        try:
            real = float(input('Digite um número real: '))
        except KeyboardInterrupt:
            print('\n\033[1:31mO usuário cancelou a operação.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[1:31mERRO! Digite um número real válido!\033[m')
        else:
            break
    return real
