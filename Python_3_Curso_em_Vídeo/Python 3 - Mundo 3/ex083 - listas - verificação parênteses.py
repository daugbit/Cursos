lista = []
exp = str(input('Digite uma expessão qualquer, utilizando parênteses: ')).strip()
for letter in exp:
    if letter == '(':
        lista.append(letter)
    elif letter == ')' and len(lista) > 0:
        lista.pop()
    elif letter == ')' and len(lista) == 0:
        lista.append(letter)
        break
if len(lista) == 0:
    print('A sua expressão está correta!')
else:
    print('A sua expressão está incorreta!')
