def voto(x):
    from datetime import date
    current_year = date.today().year
    age = current_year - x
    if age < 16:
        return f'Com {age} anos: VOTO NEGADO.'
    elif 16 >= age < 18 or age >= 65:
        return f'Com {age} anos: VOTO OPCIONAL.'
    else:
        return f'Com {age} anos: VOTO OBRIGATÓRIO.'


print(voto(int(input('Em que ano você nasceu? '))))

