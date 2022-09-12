joined_string = ''

file = '003_pi-one-million.txt'

with open(file) as file_object:
    content = file_object.readlines()

for line in content:
    joined_string += line.strip()

# print(joined_string)

if '110699' in joined_string:
    print('O seu nascimento está em Pi!')
else:
    print('O seu nascimento não está em Pi.')
