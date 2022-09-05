height = float(input('Informe a altura da parede (m): '))
width = float(input('Informe a largura da parede (m): '))
area = height * width
paint = area / 2
print(f'Para pintar esta parede de {area}m², você precisará de {paint} litros de tinta')
