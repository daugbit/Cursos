dist = float(input('Informe a distância da viagem (km): '))
if dist <= 200:
    price = dist * 0.5
    print(f'Para esta viagem de {dist}km, o preço será de R${price}')
else:
    price = dist * 0.45
    print(f'Para esta viagem de {dist}km, o preço será de R${price}')
