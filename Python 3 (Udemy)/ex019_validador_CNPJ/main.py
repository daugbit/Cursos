"""
Programa que verifique se um CNPJ informado pelo usuário é matematicamente válido ou não
"""

import cnpj

try:
    cnpj_input = cnpj.format(str(input('CNPJ: ')))

    raw_cnpj = [x for x in cnpj_input[:-2]]

    aux1 = cnpj.sequenceone(raw_cnpj)

    dig1 = cnpj.calcdigitone(raw_cnpj, aux1)

    aux2 = cnpj.sequencetwo(dig1)

    dig2 = cnpj.calcdigittwo(dig1, aux2)

    reformated = cnpj.reformat(dig2)

    if cnpj_input == reformated:
        print('\033[1:30:42mCNPJ VÁLIDO!\033[m')
    else:
        print('\033[1:30:41mCNPJ INVÁLIDO!\033[m')
except ValueError:
    print('Formato de CPJ inválido!')
