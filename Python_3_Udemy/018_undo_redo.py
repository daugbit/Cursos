tasks = []
deleted_tasks = []


def showscreen():
    print('*' * 30)
    print('[1] Adicionar nova tarefa')
    print('[2] Listar tarefas')
    print('[3] Desfazer')
    print('[4] Refazer')
    print('[5] SAIR')
    print('*' * 30)


def optionverific(option):
    if option == 1:
        return add
    elif option == 2:
        return showtasks
    elif option == 3:
        return undo
    elif option == 4:
        return redo
    elif option == 5:
        print('ATÉ LOGO!')
        return None
    else:
        print('OPÇÃO INVÁLIDA!')
        return False


def add():
    print()
    tasks.append(input('Tarefa: '))
    print('Tarefa adicionada com sucesso!')
    print()


def showtasks():
    print('\nTAREFAS:')
    for i in tasks:
        print(f'[] {i}')
    print()


def undo():
    print()
    try:
        deleted_tasks.append(tasks.pop())
        print(f'Tarefa \"{deleted_tasks[-1]}\" excluída com sucesso!')
    except IndexError:
        print('Não há tarefas a excluir.')
    print()


def redo():
    print()
    try:
        tasks.append(deleted_tasks.pop())
        print(f'Tarefa \"{tasks[-1]}\" reincluída com sucesso!')
    except IndexError:
        print('Nenhuma tarefa foi excluída.')
    print()


while True:
    showscreen()
    opt = optionverific(int(input('Escolha uma opção: ')))
    if opt is None:
        break
    opt()
