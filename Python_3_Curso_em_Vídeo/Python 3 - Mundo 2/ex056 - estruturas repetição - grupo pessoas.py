avg_age = 0
oldest_m = 0
higher20_w = 0
for c in range(1, 5):
    print(f'======{c}ª PESSOA======')
    name = str(input('Nome: '))
    gender = str(input('Gênero (F/M): '))
    age = int(input('Idade: '))
    avg_age += age
    if gender in "Mm" and age > oldest_m:
        oldest_m = age
        oldest_m_name = name
    elif gender in "Ff" and age > 20:
        higher20_w += 1
print('=' * 15)
print(f'A média de idade entre as pessoas informadas é de {avg_age / 4} anos.')
print(f'O homem mais velho entre os informados é o {oldest_m_name}, com {oldest_m} anos.')
print(f'Entre as mulheres informadas, {higher20_w} têm mais de 20 anos.')
