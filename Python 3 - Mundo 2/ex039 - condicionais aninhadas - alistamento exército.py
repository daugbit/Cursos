from datetime import date
from emoji import emojize
gender = str(input('Indique o seu gênero [m/f]: '))
if gender == "m":
    born_year = int(input('Em que ano você nasceu? '))
    current_year = date.today().year
    if current_year - born_year == 18:
        print(emojize(':yellow_circle:', language='alias'), 'Você deve se alistar neste ano!')
    elif current_year - born_year < 18:
        print(emojize(':green_circle:', language='alias'), 'Você ainda não precisa se alistar.')
        print(emojize(':point_right:', language='alias'), f'Você só precisartá se apresentar em \033[1;30;43m{born_year + 18}\033[m')
    else:
        print(emojize(':red_circle:', language='alias'), 'Já passou do prazo do seu alistamento!')
        print(emojize(':red_circle:', language='alias'), f'Você deveria ter se apresentado em \033[1;30;43m{born_year + 18}\033[m')
elif gender == "f":
    print('No Brasil, apenas pessoas do sexo MASCULINO são obrigadas a se alistar.')
else:
    print('Opção inválida.')
