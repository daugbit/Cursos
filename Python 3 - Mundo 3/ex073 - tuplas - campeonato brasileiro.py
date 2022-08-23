classific = ('Palmeiras', 'Fluminense', 'Flamengo', 'Corinthians', 'Internacional', 'Athletico-PR', 'Atlético-MG',
             'Santos', 'América-MG', 'Bragantino', 'Goiás', 'São Paulo', 'Fortaleza', 'Botafogo', 'Ceará', 'Cuiabá',
             'Avaí', 'Coritiba', 'Atlético-GO', 'Juventude')
print(classific)
print('=-=' * 50)
print('Os cinco primeiros colocados do campeonato são: ', classific[:5])
print('=-=' * 50)
print('Os quatro últimos colocados são: ', classific[:-4])
print('=-=' * 50)
print('Times em ordem alfabética: ', sorted(classific))
print('=-=' * 50)
print(f'O time do Santos está na {classific.index("Santos") + 1}ª posição.')
