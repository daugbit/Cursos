from datetime import date
adult = 0
year = date.today().year
for c in range(0, 7):
    born = int(input(f'Informe o ano de nascimento da pessoa {c+1}: '))
    if year - born >= 21:
        adult += 1
print(f'No total, {adult} pessoas já estão na maioridade.')
print(f'{7 - adult} pessoas ainda não atingiram a maioridade.')
