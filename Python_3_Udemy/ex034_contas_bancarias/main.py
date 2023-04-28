import accounts
import os

if os.name == 'nt':
    clear_command = 'cls'
else:
    clear_command = 'clear'

while True:
    os.system(clear_command)
    print('-' * 30)
    print('DAUG BANK'.center(30))
    print('-' * 30)
    print('[0] Cadastrar cliente')
    print('[1] Abrir conta')
    print('[2] Depositar')
    print('[3] Sacar')
    print('[4] Consultar saldo')
    print('[5] Alterar conta')
    print('[6] Encerrar conta')
    print('[7] SAIR')
    print('-' * 30)
    break



# account_1 = CheckingAccount(111, 222, 0, 1000)
# account_1.deposit(500)
# account_1.withdrawal(1000)
# account_1.deposit(100)
# account_1.withdrawal(100)
# account_1.deposit(5)
# account_1.withdrawal(800)
