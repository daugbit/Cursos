days = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros foram rodados? '))
price = 60 * days + 0.15 * km
print(f'O preço do aluguel será de R${price:.2f}.')
