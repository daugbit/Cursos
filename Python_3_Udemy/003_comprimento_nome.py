name = str(input('Digite o seu nome: ')).strip()
if len(name) <= 4:
    print('Seu nome é bem curto.')
elif 5 <= len(name) <= 6:
    print('Seu nomé é bem normal.')
else:
    print('Seu nome é muito comprido.')
