wage = float(input('Qual o salário atual do funcionário? R$'))
if wage >= 1250:
    print(f'O novo salário do funcionário será de R${wage * 1.1:.2f}.')
else:
    print(f'O novo salário do funcionário será de R${wage * 1.15:.2f}.')
