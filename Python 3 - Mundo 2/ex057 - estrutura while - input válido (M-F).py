gender = str(input('Informe o seu gênero (M/F): ')).strip().upper()[0]
while gender not in "MF":
    gender = str(input('informação inválida! Informe o seu gênero (M/F): ')).strip().upper()
