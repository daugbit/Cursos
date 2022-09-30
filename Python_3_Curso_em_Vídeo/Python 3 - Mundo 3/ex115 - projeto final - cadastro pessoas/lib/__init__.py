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


def linha(size=42):
    return '-' * size


def cabecalho(msg):
    print('\033[32m', linha(), sep='')
    print(msg.center(42))
    print(linha(), '\033[m')


def menu(opcoes):
    cabecalho('MENU PRINCIPAL')
    i = 1
    for item in opcoes:
        print(f'{i} - {item}')
        i += 1
    print('\033[32m', linha(), '\033[m', sep='')
    resp = leiaint('Sua opção: ')
    return resp


def fileexists(name):
    try:
        f = open(name, 'rt')
        f.close()
    except FileNotFoundError:
        return False
    else:
        return True


def filecreate(name):
    f = open(name, 'wt+')
    f.close()


def fileread(name):
    f = open(name, 'rt')
    for lines in f:
        user = lines.split(';')
        user[1] = user[1].replace('\n', '')
        print(f'{user[0]:<30}{user[1]:>3} anos')
    f.close()


def usercreate(file, name='desconhecido', age=0):
    f = open(file, 'at')
    f.write(f'{name};{age}\n')
    f.close()
    print('\033[1;33mCadastro incluído com sucesso!\033[m')
