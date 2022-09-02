import emoji
loan_value = float(input('Quanto você precisa pegar emprestado? R$'))
period = float(input('Em quantos meses você quer pagar o empréstimo? '))
wage = float(input('Qual o valor do seu salário mensal? R$'))
installment = loan_value / period
print('=-=' * 20)
if installment <= (wage * 0.3):
    print('\033[1;30;42mPARABÉNS! O seu empréstimo foi aprovado!\033[m', emoji.emojize(':money_mouth_face:', language='alias'))
    print(emoji.emojize(':point_right:', language='alias'), f'Valor total financiado: R${loan_value:.2f}')
    print(emoji.emojize(':point_right:', language='alias'), f'Número de parcelas: {period:.0f}')
    print(emoji.emojize(':point_right:', language='alias'), f'Valor de cada parcela: R${installment:.2f}')
else:
    print('\033[1;30;41mLamentamos, mas o seu empréstimo não foi aprovado\033[m', emoji.emojize(':-1:', language='alias'))
    print('O valor da parcela supera o equivalente a 30% do seu salário mensal.')
print('=-=' * 20)
