"""
Programa que verifique se um CNPJ informado pelo usuário é matematicamente válido ou não.
"""
from Python_3_Udemy.ex019_CNPJ import cnpj_param as cnpj

try:
    cnpj_input = cnpj.format(str(input('CNPJ: ')))
except ValueError:
    print('Formato de CNPJ inválido!')
else:
    if not cnpj_input:
        print('Formato de CNPJ inválido!')
    else:
        raw_cnpj = cnpj_input[:-2]
        cnpj1 = cnpj.calcdigitone(raw_cnpj)
        cnpj2 = cnpj.calcdigittwo(cnpj1)

        if cnpj_input == cnpj2:
            print('\033[1:30:42m', 'CNPJ VÁLIDO!'.center(60), '\033[m')
        else:
            print('\033[1:30:41m', 'CNPJ INVÁLIDO!'.center(60), '\033[m')
        

