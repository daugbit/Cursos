
with open('girl_names_raw.txt', 'r') as file:
    names = file.read()
    names = names.replace(' ', '').replace('\n', ';')
    names = names.split(';')

with open('girl_names.txt', 'w') as file2:
    for name in names:
        file2.write(name)
        file2.write('\n')
