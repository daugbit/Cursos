tupla = ('mestre', 'espada', 'milho', 'cachaça', 'espinho', 'calabouço', 'rosa', 'espirro', 'vagem', 'carta',
         'esquiar', 'flauta', 'esquilo', 'computador')
for word in tupla:
    print(f'\nNa palavra \033[1:33m{word}\033[m temos as seguintes vogais: ', end='')
    for letter in range(0, len(word)):
        if word[letter] in 'aeiou':
            print(word[letter], end=' ')
