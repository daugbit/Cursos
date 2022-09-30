from lib import *
from time import sleep

lista = ['Consultar cadastros', 'Novo cadastro', 'Sair do sistema']
arq = 'cadastros.txt'

if not fileexists(arq):
    filecreate(arq)

while True:
    opcao = menu(lista)
    if opcao == 1:
        cabecalho(lista[opcao - 1])
        fileread(arq)
    elif opcao == 2:
        cabecalho(lista[opcao - 1])
        name = str(input('Nome: '))
        age = int(input('Idade: '))
        usercreate(arq, name, age)
    elif opcao == 3:
        print('\033[31mAté logo!\033[m'.center(42))
        break
    else:
        print('\033[31mOpção inválida! Digite uma das opções acima!\033[m')
    sleep(1)
