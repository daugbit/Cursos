from datetime import date
current_year = date.today().year
born_year = int(input('Qual o ano de nascimento do atleta? '))
age = current_year - born_year
if age <= 9:
    print('O atleta pertence à categoria MIRIM.')
elif age <= 14:
    print('O atleta pertence à categoria INFANTIL.')
elif age <= 19:
    print('O atleta pertence à categoria JUNIOR.')
elif age <= 25:
    print('O atleta pertence à categoria SÊNIOR.')
else:
    print('O atleta pertence à categoria MASTER.')
