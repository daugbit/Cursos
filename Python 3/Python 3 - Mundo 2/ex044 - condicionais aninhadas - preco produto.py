label_price = float(input('Qual o preço de etiqueta do produto? R$'))
print('=-=' * 20)
print('''ESCOLHA UMA FORMA DE PAGAMENTO:
1 - À vista (dinheiro/cheque) - 10% de desconto
2 - À vista (cartão) - 5% de desconto
3 - Parcelado até 2x (cartão) - s/ desconto
4 - Parcelado 3x a 12x (cartão) - c/ juros de 20%''')
print('=-=' * 20)
option = int(input('Informe a forma de pagamento desejada: '))
if option == 1:
    final_price = label_price * 0.9
elif option == 2:
    final_price = label_price * 0.95
elif option == 3:
    final_price = label_price
elif option == 4:
    final_price = label_price * 1.2
else:
    final_price = 'OPÇÃO INVÁLIDA'
print('=-=' * 20)
print(f'O preço final do produto será de \033[1;30;42mR${final_price}\033[m')
