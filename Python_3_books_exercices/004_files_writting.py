from time import localtime, strftime

file = 'conteudo.txt'
start = (f'Started at {strftime("%d %b %Y %H:%M:%S", localtime())}' + '\n\n')
end = (f'Ended at {strftime("%d %b %Y %H:%M:%S", localtime())}' + '\n')
lines = ('-=' * 30 + '\n')

with open(file, 'a') as file_object:
    file_object.write(lines)
    file_object.write(start)
    file_object.write(input('Escreva algo: ') + '\n\n')
    file_object.write(end)
