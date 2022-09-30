full_name = str(input('Digite seu nome completo: ')).strip().title()
names = full_name.split()
first_name = names[0]
last_name = names[-1]
print(f'''Primeiro nome: {first_name}
Último nome: {last_name}''')
