trabalhador = {}
from datetime import date
ano = date.today().year
trabalhador['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
trabalhador['idade'] = ano - nasc
trabalhador['ctps'] = int(input('Número da CTPS (0 se não tiver): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano da contratação: '))
    trabalhador['salário'] = float(input('Salário: '))
    trabalhador['aposentadoria'] = trabalhador['contratação'] + 35 - nasc
print('=-' * 20)
for i, j in trabalhador.items():
    print(f'  - {i} tem valor {j}.')
