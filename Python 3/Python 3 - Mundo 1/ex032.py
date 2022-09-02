from datetime import date
print('=-=' * 30)
print(' ' * 28, 'ANALISADOR DE ANO BISSEXTO')
print('=-=' * 30)
year = int(input('Informe o ano que você quer analisar ou digite "0" para analisar o ano atual: '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'O ano de {year} é bissexto!')
else:
    print(f'O ano de {year} não é bissexto!')
