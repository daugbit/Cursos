while True:
    try:
        daytime = int(input('Que horas são? '))
    except ValueError:
        print('Você deve digitar apenas a hora cheia (ex.: 11, 18, 23)')
    else:
        if daytime < 0 or daytime >= 24:
            print('Horário inválido! Tente novamente.')
            continue
        if daytime < 11:
            print('BOM DIA!')
        elif daytime <= 17:
            print('BOA TARDE!')
        else:
            print('BOA NOITE!')
        break
